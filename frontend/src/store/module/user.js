import { login, logout } from '@/api/login'
import { getUser } from '@/api/user'
import { setUsername, getUsername, setToken, getToken } from '@/libs/util'

export default {
  state: {
    username: getUsername(),
    avatorImgPath: '',
    token: getToken(),
    access: [],
    hasGetInfo: false
  },
  mutations: {
    setAvator (state, avatorPath) {
      state.avatorImgPath = avatorPath
    },
    setUsername (state, name) {
      state.username = name
      setUsername(name)
    },
    setAccess (state, access) {
      state.access = access
    },
    setToken (state, token) {
      state.token = token
      setToken(token)
    },
    setHasGetInfo (state, status) {
      state.hasGetInfo = status
    }
  },
  getters: {
  },
  actions: {
    // 登录
    handleLogin ({ commit }, userdata) {
      return new Promise((resolve, reject) => {
        login(userdata).then(res => {
          const data = res.data
          commit('setUsername', userdata.username)
          commit('setToken', data.token)
          commit('setHasGetInfo', true)
          resolve()
        }).catch(err => {
          reject(err)
        })
      })
    },
    // 退出登录
    handleLogOut ({ state, commit }) {
      return new Promise((resolve, reject) => {
        commit('setUsername', '')
        commit('setAvator', '')
        commit('setToken', '')
        commit('setAccess', [])
        resolve()
      })
    },
    // 获取用户相关信息
    getUserInfo ({ state, commit }) {
      return new Promise((resolve, reject) => {
        const userinfo = {
          username: state.username
        }
        getUser(userinfo).then(res => {
          const data = res.data[0]
          commit('setAvator', data.avator)
          commit('setUsername', data.username)
          commit('setAccess', data.roles)
          resolve(data)
        }).catch(err => {
          reject(err)
        })
      })
    }
  }
}
