const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const REVIEW = 'review/'
const SEARCH = 'search/'
const SORT = 'sort/'
const COMMENT = 'comments/'
const PROFILE = 'profile/'


export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    profile: username => HOST + ACCOUNTS + PROFILE + `${username}/`,
    saveprofile: username => HOST + ACCOUNTS + PROFILE + `${username}/`+'save/',
  },
  movies:{  
    movies: () => HOST + MOVIES,
    movie_detail: movie_pk => HOST+MOVIES+`${movie_pk}/`,
    search: keyword => HOST+MOVIES+SEARCH+`${keyword}/`,
    sort: value => HOST +MOVIES+SORT+`${value}/`,
    like: movie_pk => HOST + MOVIES + 'like/' + `${movie_pk}/`,
    loadmyrivew: () => HOST + MOVIES + 'myreview/'
  },
  reviews:{
    reviews: movie_pk => HOST + MOVIES + `${movie_pk}/` + REVIEW,
    update_delete_rivew: review => HOST + MOVIES + REVIEW +`${review.id}/`,
    create_comment: comment => HOST + MOVIES + REVIEW + `${comment.review}/` + COMMENT + 'new/',
    comment_update_or_delete: comment => HOST +MOVIES +REVIEW +`${comment.review}/`+ COMMENT + `${comment.pk}/`
  }
}
