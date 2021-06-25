import axios from 'axios'
import * as appConfig from './config.json'

export const ACCESS_TOKEN_KEY = 'access_token'
export const REFRESH_TOKEN_KEY = 'refresh_token'

export const api = axios.create({
  baseURL: appConfig.api_base_url,
  responseType: 'json',
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  }
})

api.interceptors.request.use(config => {
  config.headers.authorization = localStorage.getItem(ACCESS_TOKEN_KEY)
    ? `${appConfig.jwt_prefix} ${localStorage.getItem(ACCESS_TOKEN_KEY)}`
    : ''
  return config
})

api.interceptors.response.use(
  config => config,
  async error => {
    const originalRequest = error.config
    if (error.response.status === 401 && error.config && !error.config._isRetry) {
      originalRequest._isRetry = true

      try {
        const { data } = await axios.post<{ access: string }>(
          `${appConfig.api_base_url}/jwt/refresh/`,
          { refresh: localStorage.getItem(REFRESH_TOKEN_KEY) }
        )

        localStorage.setItem(ACCESS_TOKEN_KEY, data.access)

        return api.request(originalRequest)
      } catch {
        console.log('Должен быть редирект на логин')
      }
    }
  }
)
