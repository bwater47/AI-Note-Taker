// Create a new model for the Note table.
const { Model, DataTypes } = require('sequelize');
// Import the connection to the database.
const sequelize = require('../config/connection');
// This is the Note model that extends the Sequelize Model.
class Note extends Model {}

// Define the columns in the Note table.
Note.init(
  {
    id: {
      type: DataTypes.INTEGER,
      allowNull: false,
      primaryKey: true,
      autoIncrement: true,
    },
    title: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    content: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    User_id: {
      type: DataTypes.INTEGER,
      references: {
        model: 'User',
        key: 'id',
      },
    },
  },
  {
    sequelize,
    freezeTableName: true,
    underscored: true,
    timestamps: true,
    modelName: 'Note',
  }
);

module.exports = Note;