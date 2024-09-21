import { readDatabase } from '../utils';

// const fs = require('fs');
// const path = require('path');

export default class StudentsController {
  static async getAllStudents(req, res) {
    const databaseFile = process.argv[2];
    try {
      const students = await readDatabase(databaseFile);
      let responseText = 'This is the list of our students\n';
      Object.keys(students).sort().forEach((field) => {
        responseText += `Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}\n`;
      });
      res.status(200).send(responseText.trim());
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }


  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;
  
    
    if (!major || (major !== 'CS' && major !== 'SWE')) {
      return res.status(400).json({ error: 'Major parameter must be CS or SWE' });
    }
  
    try {
      const students = await readDatabase(process.argv[2]);
  
      
      if (!students[major]) {
        return res.status(404).json({ error: 'Major not found in the database' });
      }
  
      
      return res.status(200).json(students[major]);
    } catch (error) {
        
      console.error('Error reading database:', error);
      return res.status(500).json({ error: 'Server error' });
    }
  }
  
}
