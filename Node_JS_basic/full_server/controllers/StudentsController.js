import { readDatabase } from '../utils';

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
        const databaseFile = process.argv[2];
        const major = req.params.major;

        if (major !== 'CS' && major !== 'SWE') {
            return res.status(500).send('Major parameter must be CS or SWE');
        }

        try {
            const students = await readDatabase(databaseFile);
            res.status(200).send(`List: ${students[major].join(', ')}`);
        } catch (error) {
            res.status(500).send('Cannot load the database');
        }
    }
}
