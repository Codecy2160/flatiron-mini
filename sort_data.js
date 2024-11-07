// Patient Data
const data = [
    { patient_id: "Beyonce", name: "Beyonce Knowles", age: 42, diagnosis: "Lung Cancer", severity: "High", diagnosis_date: "2024-10-01", last_checkup_date: "2024-10-20" },
    { patient_id: "Diddy", name: "Sean Combs", age: 54, diagnosis: "Breast Cancer", severity: "Moderate", diagnosis_date: "2024-05-15", last_checkup_date: "2024-08-10" },
    { patient_id: "Rihanna", name: "Rihanna Fenty", age: 35, diagnosis: "Colorectal Cancer", severity: "Low", diagnosis_date: "2023-12-01", last_checkup_date: "2024-02-18" },
    { patient_id: "JayZ", name: "Jay-Z Carter", age: 54, diagnosis: "Prostate Cancer", severity: "High", diagnosis_date: "2024-07-23", last_checkup_date: "2024-10-05" }
];
 
// Function  sort patients by a given attribute
function sortPatients(patients, attribute, ascending = true) {
    return patients.sort((a, b) => {
        if (ascending) {
            return a[attribute] < b[attribute] ? -1 : a[attribute] > b[attribute] ? 1 : 0;
        } else {
            return a[attribute] > b[attribute] ? -1 : a[attribute] < b[attribute] ? 1 : 0;
        }
    });
}
 
// Sort patients by diagnosis_date
const sortedByDiagnosisDate = sortPatients(data, "diagnosis_date", true);
console.log("Sorted by Diagnosis Date:\n", sortedByDiagnosisDate);
 
// Sort patients by severity 
const severityOrder = { "Low": 0, "Moderate": 1, "High": 2 };
data.forEach(patient => {
    patient.severity_level = severityOrder[patient.severity];
});
const sortedBySeverity = sortPatients(data, "severity_level", false);
console.log("Sorted by Severity:\n", sortedBySeverity);
 
// Additional sorting based on age (oldest patients first)
const sortedByAge = sortPatients(data, "age", false);
console.log("Sorted by Age:\n", sortedByAge);