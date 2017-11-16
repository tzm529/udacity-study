# -*- coding:utf-8 -*-  
import fresh_tomatoes
import media

justice_league = media.Movie("正义联盟",
						"受到超人无私奉献的影响，蝙蝠侠重燃了对人类的信心，接受了新盟友",
						"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2504027804.jpg",
						"http://v.youku.com/v_show/id_XMzE1Mzg4MTEyNA==.html")

avatar = media.Movie("阿凡达",
						"本片采用3D技术拍摄，共耗资5亿美元制作发行，是电影史上最为昂贵的作品",
						"https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2180085848.jpg",
						"http://v.youku.com/v_show/id_XMTk4ODUyNDQ4.html")

thor = media.Movie("雷神3：诸神黄昏",
						"雷神3：诸神黄昏 Thor: Ragnarok (2017)",
						"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2500451074.jpg",
						"http://v.youku.com/v_show/id_XMzEwNDY0Mjg2MA==.html")

golden_monk = media.Movie("降魔传",
						"南宋年间，杭州城妖怪肆虐，百姓困苦不堪",
						"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2503850915.jpg",
						"http://v.youku.com/v_show/id_XMzEyNzE3MDUwMA==.html")

beast = media.Movie("狂兽 狂獸",
						"重案督察西狗（张晋 饰）与搭档阿德（吴樾 饰）到某渔村追捕涉嫌多桩凶案的歹徒江贵成",
						"https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2502374737.jpg",
						"http://v.youku.com/v_show/id_XMTUwMjMyOTA1Mg==.html")

storm = media.Movie("暴雪将至",
						"上世纪九十年代某个小城，天气预报中一场百年不遇的暴雪即将侵袭此地",
						"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2504884681.jpg",
						"http://v.youku.com/v_show/id_XMzE1NTg4MjI3Ng==.html")

movies = [justice_league, avatar, thor, golden_monk, beast, storm]
fresh_tomatoes.open_movies_page(movies)