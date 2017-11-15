# -*- coding:utf-8 -*-  
import fresh_tomatoes
import media

movie_1 = media.Movie("正义联盟", "受到超人无私奉献的影响，蝙蝠侠重燃了对人类的信心，接受了新盟友", "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2504027804.jpg", "http://v.youku.com/v_show/id_XMzE1Mzg4MTEyNA==.html")
movie_2 = media.Movie("东方快车谋杀案", "东方快车谋杀案 Murder on the Orient Express", "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2502165084.jpg", "http://v.youku.com/v_show/id_XMzExMDQzOTkyMA==.html")
movie_3 = media.Movie("雷神3：诸神黄昏", "雷神3：诸神黄昏 Thor: Ragnarok (2017)", "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2500451074.jpg", "http://v.youku.com/v_show/id_XMzEwNDY0Mjg2MA==.html")
movie_4 = media.Movie("降魔传", "南宋年间，杭州城妖怪肆虐，百姓困苦不堪", "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2503850915.jpg", "http://v.youku.com/v_show/id_XMzEyNzE3MDUwMA==.html")
movie_5 = media.Movie("狂兽 狂獸", "重案督察西狗（张晋 饰）与搭档阿德（吴樾 饰）到某渔村追捕涉嫌多桩凶案的歹徒江贵成", "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2502374737.jpg", "http://v.youku.com/v_show/id_XMTUwMjMyOTA1Mg==.html")
movie_6 = media.Movie("暴雪将至", "上世纪九十年代某个小城，天气预报中一场百年不遇的暴雪即将侵袭此地", "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2504884681.jpg", "http://v.youku.com/v_show/id_XMzE1NTg4MjI3Ng==.html")

movies = [movie_1, movie_2, movie_3, movie_4, movie_5, movie_6]
fresh_tomatoes.open_movies_page(movies)