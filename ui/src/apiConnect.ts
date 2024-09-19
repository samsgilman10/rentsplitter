import axios from 'axios';

axios.defaults.baseURL = import.meta.env.VITE_API_URL;

export async function postNewSession(name: string, roomLabels: string[]) {
    axios.post('/new-session', {
        name,
        roomLabels,
    })
}