import axios from 'axios'
import * as config from './config.json'

export const api = axios.create({
  baseURL: config.api_base_url,
  responseType: 'json',
  headers: {
    'authorization': localStorage.getItem('token_access') ? `${config.jwt_prefix} ${localStorage.getItem('token_access')}` : '',
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  }
})

