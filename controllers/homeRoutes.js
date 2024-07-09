const router = require('express').Router();
const { Note, User } = require('../models');
// Create a new route that will render the homepage.
router.get('/', async (req, res) => {
  try {
    // Get all the notes and join them with the user data.
    const noteData = await Note.findAll({
      include: [
        {
          model: User,
          attributes: ['username'],
        },
      ],
    });
    // Serialize the data so the template can read it.
    const notes = noteData.map((note) => note.get({ plain: true }));
    // Render the homepage.
    res.render('home', {
      notes,
    });
  } catch (err) {
    res.status(500).json(err);
  }
});

module.exports = router;