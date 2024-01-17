/*
    This script creates users with different permissions.
*/

print("Started Adding Users.");

db = db.getSiblingDB("admin");
db.createRole({
    role: "readWriteCommands",
    privileges: [
    {
      resource: { db: "Security_Audit", collection: "Commands" },
      actions: ["find", "insert", "update", "remove"]
    }
  ],
  roles: []
});

db.createRole({
    role: "readCommands",
    privileges: [
    {
      resource: { db: "Security_Audit", collection: "Commands" },
      actions: ["find"]
    }
  ],
  roles: []
});

db.createRole({
    role: "readWriteLogin",
    privileges: [
    {
      resource: { db: "Security_Audit", collection: "Login" },
      actions: ["find", "insert", "update", "remove"]
    }
  ],
  roles: []
});

db.createRole({
    role: "readLogin",
    privileges: [
    {
      resource: { db: "Security_Audit", collection: "Login" },
      actions: ["find"]
    }
  ],
  roles: []
});

db.createRole({
    role: "readWriteResults",
    privileges: [
    {
      resource: { db: "Security_Audit", collection: "Audit_Results" },
      actions: ["find", "insert", "update", "remove"]
    }
  ],
  roles: []
});

db.createRole({
    role: "readResults",
    privileges: [
    {
      resource: { db: "Security_Audit", collection: "Audit_Results" },
      actions: ["find"]
    }
  ],
  roles: []
});

db.createUser(
   {
     user: "CommandReadWrite",
     pwd: "CMDWRITE",
     roles: ["readWriteCommands"]
   }
);

db.createUser(
   {
     user: "CommandRead",
     pwd: "CMDREAD",
     roles: ["readCommands"]
   }
);

db.createUser(
   {
     user: "LoginReadWrite",
     pwd: "LOGINWrite",
     roles: ["readWriteLogin"]
   }
);

db.createUser(
   {
     user: "LoginRead",
     pwd: "LOGINRead",
     roles: ["readLogin"]
   }
);

db.createUser(
   {
     user: "AuditReadWrite",
     pwd: "AUDITWrite",
     roles: ["readWriteResults"]
   }
);

db.createUser(
   {
     user: "AuditRead",
     pwd: "AUDITRead",
     roles: ["readResults"]
   }
);

db = db.getSiblingDB("Security_Audit");

db.createCollection('Login');

// 7|/S!~t8Z"E3&>Nm
db.Login.insertOne({
    "username": "ISS_ADMIN",
    "password": "$2b$12$.UDCL2JU7zsm0R.LlQKiJe2GXugySqEo4zIISwQLdKmkIYO34Q.u.",
    "active": true,
    "email": "informationssicherheit@iu.org",
})


print("End Adding Users.");