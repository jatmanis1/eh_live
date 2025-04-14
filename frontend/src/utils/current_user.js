// utils/currentUser.js
export function currentUser() {
    const user = localStorage.getItem('user');
    return JSON.parse(user);  // Parse and return the user object from localStorage
}
