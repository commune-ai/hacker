
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());

mongoose.connect('mongodb://mongodb:27017/server-marketplace', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define routes here

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
