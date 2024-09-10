
import asyncio
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

app = FastAPI()

model_name = "mattshumer/Reflection-70B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")

class GenerationRequest(BaseModel):
    prompt: str
    max_length: int = 100
    temperature: float = 0.7
    top_p: float = 0.9

async def generate_text(prompt, max_length, temperature, top_p):
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(model.device)
    
    for i in range(max_length):
        with torch.no_grad():
            outputs = model.generate(
                input_ids,
                max_length=input_ids.shape[1] + 1,
                num_return_sequences=1,
                do_sample=True,
                temperature=temperature,
                top_p=top_p,
                pad_token_id=tokenizer.eos_token_id,
            )
        
        new_token = outputs[0][-1].unsqueeze(0)
        input_ids = torch.cat([input_ids, new_token], dim=-1)
        
        yield tokenizer.decode(new_token[0], skip_special_tokens=True)
        
        if new_token.item() == tokenizer.eos_token_id:
            break
        
        await asyncio.sleep(0.1)  # Add a small delay to simulate streaming

@app.post("/generate")
async def generate(request: GenerationRequest):
    try:
        return StreamingResponse(
            generate_text(request.prompt, request.max_length, request.temperature, request.top_p),
            media_type="text/plain",
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
