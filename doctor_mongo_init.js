db = db.getSiblingDB("admin");
db.auth(
  process.env.MONGO_INITDB_ROOT_USERNAME,
  process.env.MONGO_INITDB_ROOT_PASSWORD
);
db = db.getSiblingDB(process.env.MONGO_INITDB_DATABASE);
db.createCollection("doctor");

db.doctor.insertMany([
  {
    id: "1",
    firstName: "Muhammad Ali",
    lastName: "Kahoot",
    speciality: "DevOps",
  },
  { id: "2", firstName: "Good", lastName: "Doctor", speciality: "Test" },
]);
// //db = db.getSiblingDB("admin");

// // Create root user with provided credentials
// // db.createUser({
// //   user: "admin",
// //   pwd: "password",
// //   roles: [{ role: "root", db: "admin" }],
// // });

// // // Switch to desired database
// // db = db.getSiblingDB("my_database");

// // // Create a test collection and insert test data
// // db.testCollection.insertMany([
// //   { name: "Alice", age: 25 },
// //   { name: "Bob", age: 30 },
// // ]);

// // db.createUser({
// //   user: "pastime",
// //   pwd: "pastime123",
// //   roles: [
// //     {
// //       role: "readWrite",
// //       db: "pastime",
// //     },
// //   ],
// // });

// db = db.getSiblingDB("");

// db.testCollection.insertMany([
//   { name: "Alice", age: 25 },
//   { name: "Bob", age: 30 },
// ]);
