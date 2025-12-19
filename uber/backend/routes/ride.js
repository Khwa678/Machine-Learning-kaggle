const auth = require("../middleware/auth");

router.post("/book", auth, async (req, res) => {
  const { pickup, drop } = req.body;
  const ride = await Ride.create({ pickup, drop });
  res.json(ride);
});
