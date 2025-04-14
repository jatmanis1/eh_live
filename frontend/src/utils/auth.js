// import jwtdecode from 'jwt-decode'

import * as jwtDecodeImport from "jwt-decode";

// import { Connect, fetchModule } from 'vite'
// const jwtDecode = require('jwt-decode');
const jwtDecode = jwtDecodeImport.default || jwtDecodeImport;
export function isAuthenticated() {
    const token = localStorage.getItem('token')
    console.log('ghjkl', token)
    if (!token) { console.log('no token found'); return false;}
    try {
        // const { exp } = jwtDecode(token);

        // print(exp)
        if (!token) {
            localStorage.removeItem('token')
            localStorage.removeItem('user')
            console.log('token not found or expired');
            return false;

        }
        return true;

    }
    catch (error) {
        console.log('error', error)
        localStorage.removeItem('user')
        localStorage.removeItem('token')
        console.log('token have error')

        return false;

    }

}
