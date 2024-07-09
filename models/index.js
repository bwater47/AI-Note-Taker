// Import the Models.
const User = require("./User");
const Note = require("./Note");

// User have many Notes
User.hasMany(Note, {
  foreignKey: "user_id",
  onDelete: "CASCADE",
});
// Note belongs to User
Note.belongsTo(User, {
  foreignKey: "user_id",
});

module.exports = { User, Note };
