const mongoose = require("mongoose");

const rideSchema = new mongoose.Schema({
  pickup: String,
  drop: String,
  status: {
    type: String,
    default: "requested",
  },
  createdAt: {
    type: Date,
    default: Date.now,
  },
});

module.exports = mongoose.model("Ride", rideSchema);
