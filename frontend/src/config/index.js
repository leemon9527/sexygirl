export default {
  /**
   * @description 配置显示在浏览器标签的title
   */
  title: '彩票之王',
  /**
   * @description token在Cookie中存储的天数，默认7天
   */
  cookieExpires: 1,
  /**
   * @description 是否使用国际化，默认为false
   *              如果不使用，则需要在路由中给需要在菜单中展示的路由设置meta: {title: 'xxx'}
   *              用来在菜单中显示文字
   */
  useI18n: true,
  /**
   * @description 默认打开的首页的路由name值，默认为home
   */
  homeName: 'home',
  /**
   * @description api请求基础路径
   */
  baseUrl: {
    dev: '',
    pro: 'http://oms.itgo88.com'
  },

  // 表格数据
  LIMIT: 10,
  pagesize: [10, 20, 50, 100],
  pageformat: 'total, prev, pager, next, sizes',

  // 本地上传到服务器
  fileuploads: '/api/fileuploads/',

  // 登录
  login: '/api/api-token-auth/',
  changePassword: '/api/changepasswd/',

  // 用户
  users: '/api/users/',
  groups: '/api/groups/',
  roles: '/api/roles/',

  // tools
  uploads: '/api/upload/',

  // prediction
  news: '/api/news/',
  games: '/api/games/',
  pregames: '/api/pregames/',
  predictions: '/api/predictions/',
  spiderrecords: '/api/spiderrecords/',
  gvcount: '/api/gvcount/',
  zcj: '/api/zcj/',
  cp: '/api/cp/',
  zcj_socre: '/api/zcj_socre/',

  // teams
  leagues: '/api/leagues/',
  teams: '/api/teams/'
}
