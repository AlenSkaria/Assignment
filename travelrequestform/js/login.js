let userData = {
  users: [
    {
      userId: 1,
      username: "alonn",
      password: "123",
      role: "employee",
      firstName: "alonn",
      lastName: "grey",
      email: "a@gmail.com",
      phoneNumber: "978451214",
    },
    {
      userId: 2,
      username: "aiden",
      password: "1",
      role: "employee",
      firstName: "aiden",
      lastName: "grey",
      email: "ai@gmail.com",
      phoneNumber: "98781214",
    },
    {
      userId: 3,
      username: "admin",
      password: "12",
      role: "admin",
    },
  ],
};

function login() {
  event.preventDefault();
  let userName = document.getElementById("userName").value;
  let password = document.getElementById("password").value;
  const userFound = userData.users.find(
    (user) => user.username === userName && user.password === password
  );
  console.log(userFound);
  if (userFound) {
    localStorage.setItem("loggedUser", JSON.stringify(userFound));
    if (userFound.role === "admin") {
      window.location.href = "../pages/adminPage.html";
    } else if (userFound.role === "employee") {
      window.location.href = "../pages/employeePage.html";
    }
  } else {
    const warning = document.querySelector(".warning");
    warning.innerHTML = "😥Sorry! No user found";
    warning.classList.remove("hide");
    setTimeout(() => {
      warning.classList.add("hide");
    }, 1000);
  }
}

document.addEventListener("DOMContentLoaded", () => {
  localStorage.setItem("usersList", JSON.stringify(userData));
});
