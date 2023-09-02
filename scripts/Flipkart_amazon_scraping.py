from bs4 import BeautifulSoup
import requests

'''Here we are SCRAPING the top products of a category if the person SELECTS a category and 
   than wants the top selling or trending products '''


# url = "https://www.amazon.in/gp/bestsellers/apparel/1968120031/ref=zg_bs_nav_apparel_2_1968024031"
# url = "https://www.amazon.in/gp/bestsellers/apparel/1968122031/ref=zg_m_bs_nav_apparel_3_1968120031"
d = {'classic_suit': 'https://www.amazon.in/gp/bestsellers/apparel/1968107031/ref=zg_bs_nav_apparel_2_1968024031',
     'jackets': 'https://www.amazon.in/gp/bestsellers/apparel/1968088031/ref=zg_bs_nav_apparel_3_29945464031',
     'kurta_men': 'https://www.amazon.in/gp/bestsellers/apparel/3723382031/ref=zg_bs_nav_apparel_3_1968248031',
     'lehenga': 'https://www.amazon.in/gp/bestsellers/apparel/3723378031/ref=zg_bs_nav_apparel_3_1968253031',
     'nehru_jackets': 'https://www.amazon.in/s?k=nehru+jacket+for+men&crid=2D2ZNGED8WKJI&sprefix=nehru+jacket+for+men%2Caps%2C275&ref=nb_sb_noss_1',
     'saree': 'https://www.amazon.in/gp/bestsellers/apparel/1968256031/ref=zg_bs_nav_apparel_3_1968253031',
     'sherwanis': 'https://www.amazon.in/gp/bestsellers/apparel/1968251031/ref=zg_bs_nav_apparel_3_1968248031',
     'shoes': 'https://www.amazon.in/gp/bestsellers/shoes/1983577031?ref_=Oct_d_obs_S&pd_rd_w=vo0BK&content-id=amzn1.sym.6c2129e0-dd81-4530-ab42-0f0d524cd085&pf_rd_p=6c2129e0-dd81-4530-ab42-0f0d524cd085&pf_rd_r=EDSZFMRZ3JGNFXX39KA8&pd_rd_wg=seEkk&pd_rd_r=25613ea3-a20d-4fe6-8342-114723cf425e',
     'tshirt': 'https://www.amazon.in/gp/bestsellers/apparel/1968123031/ref=zg_bs_nav_apparel_3_1968120031'}

d2 = {
    'classic_suit': 'https://www.flipkart.com/clothing-and-accessories/blazers-suits-waistcoat-coat/pr?sid=clo%2Cupk&otracker=categorytree&p%5B%5D=facets.ideal_for%255B%255D%3DMen&otracker=nmenu_sub_Men_0_Suits%2C%20Blazers%20%26%20Waistcoats',
    'jackets': 'https://www.flipkart.com/clothing-and-accessories/winter-wear/jackets/men-jackets/pr?sid=clo,qvw,z0g,jbm&otracker=categorytree&otracker=nmenu_sub_Men_0_Jackets',
    'kurta_men': 'https://www.flipkart.com/clothing-and-accessories/ethnic-wear/ethnic-sets/men-ethnic-sets/pr?sid=clo,cfv,itg,pme&otracker=categorytree&otracker=nmenu_sub_Men_0_Ethnic%20Sets',
    'lehenga': 'https://www.flipkart.com/clothing-and-accessories/lehenga-choli/women-lehenga-choli/pr?sid=clo,hlg,wrp&otracker=categorytree&otracker=nmenu_sub_Women_0_Lehenga%20Choli',
    'nehru_jackets': 'https://www.flipkart.com/search?q=nehru+jacket+for+men&sid=clo%2Cqvw%2Cz0g%2Cjbm&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_17_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_17_na_na_na&as-pos=1&as-type=RECENT&suggestionId=nehru+jacket+for+men%7CMen%27s+Jackets&requestId=0ee0eba5-af88-450a-9bbe-35d7b2832dc1&as-searchtext=nehru%20jackets%20for',
    'saree': 'https://www.flipkart.com/clothing-and-accessories/saree-and-accessories/saree/women-saree/pr?sid=clo,8on,zpd,9og&otracker=categorytree&otracker=nmenu_sub_Women_0_Sarees',
    'sherwanis': 'https://www.flipkart.com/clothing-and-accessories/ethnic-wear/sherwani/men-sherwani/pr?sid=clo,cfv,dra,brt&otracker=categorytree&otracker=nmenu_sub_Men_0_Sherwanis',
    'shoes': 'https://www.flipkart.com/mens-footwear/casual-shoes/sneakers~type/pr?sid=osp%2Ccil%2Ce1f&otracker=nmenu_sub_Men_0_Sneakers',
    'tshirt': 'https://www.flipkart.com/clothing-and-accessories/topwear/tshirt/men-tshirt/pr?sid=clo,ash,ank,edy&otracker=categorytree&otracker=nmenu_sub_Men_0_T-Shirts'}


def getProducts(category):
    url = d[category]
    url2 = d2[category]
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    if category == 'nehru_jackets':
        top_product_elements = soup.find_all('h2', class_='a-size-mini a-spacing-none a-color-base s-line-clamp-2')
    else:
        top_product_elements = soup.find_all('div', class_='_cDEzb_p13n-sc-css-line-clamp-3_g3dy1')
    l = []
    c = 0
    for product_element in top_product_elements:
        c = c + 1
        product_name = product_element.text.strip()
        l.append(product_name)
        if c >= 10:
            break

    response = requests.get(url2)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    top_product_elements = soup.find_all('a', class_="IRpwTa")
    c = 0
    for product_element in top_product_elements:
        c = c + 1
        product_name = product_element.text.strip()
        l.append(product_name)
        if c >= 10:
            break
    return l
