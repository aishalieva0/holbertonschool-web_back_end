export default function createEmployeesObject(departmentName, employees) {
  const employeesObj = {};
  employeesObj[departmentName] = employees;
  return employeesObj;
}
