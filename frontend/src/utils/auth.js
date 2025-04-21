// // import jwtdecode from 'jwt-decode'

// import * as jwtDecodeImport from "jwt-decode";

// // import { Connect, fetchModule } from 'vite'
// // const jwtDecode = require('jwt-decode');
// const jwtDecode = jwtDecodeImport.default || jwtDecodeImport;
// export function isAuthenticated() {
//     const token = localStorage.getItem('token')
//     console.log('ghjkl', token)
//     if (!token) { console.log('no token found'); return false; }
//     try {
//         // const { exp } = jwtDecode(token);

//         // print(exp)
//         if (!token) {
//             localStorage.removeItem('token')
//             localStorage.removeItem('user')
//             console.log('token not found or expired');
//             return false;

//         }
//         return true;

//     }
//     catch (error) {
//         console.log('error', error)
//         localStorage.removeItem('user')
//         localStorage.removeItem('token')
//         console.log('token have error')

//         return false;

//     }

// }


import * as jwtDecodeImport from "jwt-decode";
// const jwtDecode = jwtDecodeImport.default || jwtDecodeImport;

export function isAuthenticated() {
    const token = localStorage.getItem('token');
    const user = JSON.parse(localStorage.getItem('user'));
    const expiry = localStorage.getItem('tokenExpiry');

    // Check if all exist
    if (!token || !user || !expiry) {
        alert('Missing token, user, or expiry.');
        clearAuthStorage();
        return false;
    }

    // Check expiry time
    if (Date.now() > parseInt(expiry)) {
        alert('Token expired.');
        clearAuthStorage();
        return false;
    }
    console.log(Date.now(), parseInt(expiry))
    // alert('tokenn and expiry found')
    // Optionally: Decode token and check if it's valid
    // try {
    // const decoded = jwtDecode(token);
    // console.log('Decoded JWT:', decoded); // optional
    return true;
    // } catch (error) {
    //     console.log('Token decoding failed:', error);
    //     clearAuthStorage();
    //     return false;
    // }
}

// 🔧 Utility function to clear all auth-related data
function clearAuthStorage() {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    localStorage.removeItem('tokenExpiry');
}
