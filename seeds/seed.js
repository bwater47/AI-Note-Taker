// Import the sequelize connection, the User model, and the Note model, and the data from the JSON files.
const sequelize = require("../config/connection");
const { User, Note } = require("../models");
const userData = require("./userData.json");
const NoteData = require("./noteData.json");
// Define the function that will seed the database.
const seedDatabase = async () => {
  await sequelize.sync({ force: true });
  // Use the bulkCreate method to insert the data into the database.
  await User.bulkCreate(userData, {
    individualHooks: true,
    returning: true,
  });

  await Note.bulkCreate(NoteData, {
    individualHooks: true,
    returning: true,
  });
  // Exit the process when the data is inserted.
  process.exit(0);
};
// Call the function to seed the database.
seedDatabase();
