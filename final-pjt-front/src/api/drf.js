const HOST = 'http://localhost:8001/api/v1/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const REVIEWS = 'reviews/'
const SEARCH = 'search/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
  },
  movies:{
    movies: () => HOST + MOVIES,
    movie_detail: movie_pk => HOST+MOVIES+`${movie_pk}/`,
    search: keyword => HOST+MOVIES+SEARCH+`${keyword}/`
  },
  reviews:{
    reviews: movie_pk => HOST + MOVIES + `${movie_pk}/` + REVIEWS
  }
}
