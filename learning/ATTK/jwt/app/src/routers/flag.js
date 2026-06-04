const express = require('express');
const router = express.Router();

const flag = process.env.FLAG || "FLAG{fake_flag}";

router.get('/flag', (req, res) => {
  if (req.user && req.user.username === "admin") {
    return res.render("flag", { flag });
  }
  return res.status(403).send("Forbidden");
});

module.exports = router;
