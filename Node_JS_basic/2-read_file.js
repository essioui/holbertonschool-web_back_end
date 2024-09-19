const fs = require('fs');

function countStudents(path) {
  try {
    // قراءة ملف CSV بشكل متزامن
    const data = fs.readFileSync(path, 'utf8');

    // تقسيم البيانات إلى صفوف
    const rows = data.trim().split('\n');
    
    // التحقق من أن الصفوف تحتوي على بيانات
    if (rows.length === 0) {
      throw new Error('Cannot load the database');
    }

    // استخراج رؤوس الأعمدة
    const headers = rows[0].split(',');
    if (headers[0] !== 'firstname' || headers[1] !== 'lastname' || headers[2] !== 'age' || headers[3] !== 'field') {
      throw new Error('Invalid CSV format');
    }

    // إعداد هيكل البيانات لتخزين الطلاب حسب المجال
    const students = {};
    let totalStudents = 0;

    // قراءة بيانات الطلاب
    for (let i = 1; i < rows.length; i++) {
      const fields = rows[i].split(',');
      if (fields.length < 4 || fields.some(field => field.trim() === '')) {
        continue; // تجاهل الصفوف غير الصالحة
      }
      const [firstname, lastname, age, field] = fields;
      if (!students[field]) {
        students[field] = [];
      }
      students[field].push(firstname);
      totalStudents++;
    }

    // طباعة عدد الطلاب الإجمالي
    console.log(`Number of students: ${totalStudents}`);

    // طباعة عدد الطلاب في كل مجال
    for (const [field, names] of Object.entries(students)) {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }

  } catch (err) {
    // التعامل مع الأخطاء مثل عدم وجود الملف
    console.error('Cannot load the database');
  }
}

module.exports = countStudents;
