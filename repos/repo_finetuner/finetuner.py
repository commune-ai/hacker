
import os
from transformers import AutoModelForSequenceClassification, AutoTokenizer, Trainer, TrainingArguments
from datasets import load_dataset

class Finetuner:
    def __init__(self):
        self.tasks = {}

    def start_finetuning(self, model_name, data_path):
        task = FinetuningTask(model_name, data_path)
        self.tasks[task.id] = task
        task.start()
        return task

    def get_task(self, task_id):
        return self.tasks.get(task_id)

class FinetuningTask:
    def __init__(self, model_name, data_path):
        self.id = os.urandom(16).hex()
        self.model_name = model_name
        self.data_path = data_path
        self.status = "pending"
        self.progress = 0

    def start(self):
        self.status = "running"
        self._finetune()

    def _finetune(self):
        # Load dataset
        dataset = load_dataset('text', data_files=self.data_path)

        # Load model and tokenizer
        model = AutoModelForSequenceClassification.from_pretrained(self.model_name)
        tokenizer = AutoTokenizer.from_pretrained(self.model_name)

        # Tokenize dataset
        def tokenize_function(examples):
            return tokenizer(examples["text"], padding="max_length", truncation=True)

        tokenized_datasets = dataset.map(tokenize_function, batched=True)

        # Set up training arguments
        training_args = TrainingArguments(
            output_dir="./results",
            num_train_epochs=3,
            per_device_train_batch_size=8,
            per_device_eval_batch_size=8,
            warmup_steps=500,
            weight_decay=0.01,
            logging_dir="./logs",
        )

        # Initialize Trainer
        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=tokenized_datasets["train"],
        )

        # Start training
        trainer.train()

        self.status = "completed"
        self.progress = 100
