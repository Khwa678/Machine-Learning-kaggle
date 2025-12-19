const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
require("dotenv").config();

const app = express();

/* ✅ MIDDLEWARE */
app.use(cors());
app.use(express.json());

/* ✅ ROUTES */
const authRoutes = require("./routes/auth");
const rideRoutes = require("./routes/ride");

app.use("/api/auth", authRoutes);
app.use("/api/ride", rideRoutes);

/* ✅ DATABASE */
mongoose
  .connect("mongodb://127.0.0.1:27017/zyro")
  .then(() => console.log("MongoDB Connected"))
  .catch((err) => console.log("Mongo Error:", err));

/* ✅ TEST ROUTE */
app.get("/", (req, res) => {
  res.send("ZYRO Backend Running 🚀");
});

/* ✅ START SERVER */
app.listen(5000, () => {
  console.log("Server running on port 5000");
});
