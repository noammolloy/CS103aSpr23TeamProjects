const express = require('express');
const router = express.Router();
const User = require('../models/User')
const axios = require('axios')

isLoggedIn = (req,res,next) => {
    if (res.locals.loggedIn) {
      next()
    } else {
      res.redirect('/login')
    }
  }

router.get('/sydney/',
  isLoggedIn,
  async (req, res, next) => {
            const r = "";
            res.render('sydney', {r});
});

router.post('/sydney',
  isLoggedIn,
  async (req, res, next) => {
      const prompt = "Create a short story under 200 words using these input keywords about dinosaurs: ".concat(req.body.prompt);
      const response = await axios.post('https://api.openai.com/v1/engines/text-davinci-003/completions', {
        prompt: prompt,
        max_tokens: 3900,
        
      }, {
        headers: {
          'Authorization': `Bearer ${process.env.APIKEY}`,
        },
      });
      const r = clean(response.data.choices[0].text.trim());

      res.render('sydney', {r})
});

function clean(str) {
  const index = str.indexOf('\n');
  if (index === -1) {
    return null; // return null if no newline is found
  }
  return str.slice(index + 1);
}

module.exports = router;