// import jwtdecode from 'jwt-decode'

import * as jwtDecodeImport from "jwt-decode";

// import { Connect, fetchModule } from 'vite'
// const jwtDecode = require('jwt-decode');
const jwtDecode = jwtDecodeImport.default || jwtDecodeImport;
export function isAuthenticated() {
    const token = localStorage.getItem('token')
    console.log('ghjkl', token)
    if (!token) return false;
    try {
        // const { exp } = jwtDecode(token);

        // print(exp)
        if (!token) {
            localStorage.removeItem('token')
            localStorage.removeItem('user')
            return false;

        }
        return true;

    }
    catch (error) {
        console.log('error', error)
        localStorage.removeItem('user')
        localStorage.removeItem('token')
        return false;

    }

}