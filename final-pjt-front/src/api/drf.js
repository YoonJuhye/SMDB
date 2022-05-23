const HOST = 'http://localhost:8001/api/v1/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
  },
  movies:{
    movies: () => HOST + MOVIES,
    movie_detail: movie_pk => HOST+MOVIES+`${movie_pk}/`
  }
}
