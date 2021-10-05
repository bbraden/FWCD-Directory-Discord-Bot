from discord.message import PartialMessage
from get_token import getToken
import discord
from discord.ext import commands
import selenium
from selenium import webdriver
import os
from time import sleep, time
import json
import requests
import random
from selenium.webdriver.common.by import By
from btc import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

client = commands.Bot(command_prefix=">")

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome(executable_path="/Users/braden/duck/melon/chromedriver 2")

checkEmoji = '✅'
xEmoji = '❎'


@client.event
async def on_ready():
    driver.get("https://www.google.com/")
    print("🍉")


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


@client.command()
async def quote(ctx):
    quote = get_quote()
    await ctx.send(quote)

@client.command()
async def openbrower(ctx):
    driver.get('https://www.google.com/')


@client.command()
async def on_reaction_add(reaction, ctx):
    channel = reaction.message.channel
    await ctx.send('ty')


@client.command(aliases=['cmd'])
async def cmds(ctx):
    await ctx.send('commands: >info <firstName> <lastName>, >personfind <firstName> <lastName>')


@client.command(aliases=['bitcoin'])
async def btc(ctx):
    price = get_btc_price()
    embed = discord.Embed(title='btc price')
    embed.set_footer(text='$' + price)
    await ctx.send(embed=embed)


@client.command(aliases=['momfindusage', 'mu', 'momu', 'musage'])
async def momusage(ctx):
    embed = discord.Embed(title='>mom <kid first name> <kid last name>')
    await ctx.send(embed=embed)


@client.command(aliases=['pf', 'fp', 'findperson', 'fwcdlookup'])
async def personfind(ctx, arg1, arg2):
    driver.delete_all_cookies()
    firstName = arg1
    lastName = arg2
    driver.get("https://fwcd.myschoolapp.com/app#login")
    sleep(5)
    try:
        username = driver.find_element_by_xpath("""//*[@id="Username"]""").send_keys('bradenbaker25')
    except:
        driver.get('https://fwcd.myschoolapp.com/app/student#directory/1412')
    sleep(1)
    try:
        nextbtn = driver.find_element_by_xpath("""//*[@id="nextBtn"]""").click()
    except:
        driver.get('https://fwcd.myschoolapp.com/app/student#directory/1412')
    sleep(1)
    try:
        password = driver.find_element_by_xpath("""//*[@id="Password"]""").send_keys('Cb575757')
    except:
        driver.get('https://fwcd.myschoolapp.com/app/student#directory/1412')
    sleep(1)
    try:
        loginbtn = driver.find_element_by_xpath("""//*[@id="loginBtn"]""").click()
    except:
        driver.get('https://fwcd.myschoolapp.com/app/student#directory/1412')
    sleep(3)
    driver.get('https://fwcd.myschoolapp.com/app/student#directory/1412')
    sleep(4)
    searchbox1 = driver.find_element_by_xpath("""//*[@id="search-text-box"]""").send_keys(firstName + ' ' + lastName)
    sleep(1)
    searchbtn = driver.find_element_by_xpath("""//*[@id="search-directory-button"]""").click()
    sleep(2)
    personName = driver.find_element_by_xpath("""//*[@id="directory-items-container"]/tbody/tr/td[2]/div[2]/h3""").text
    img1 = driver.find_element_by_xpath("""//*[@id="directory-items-container"]/tbody/tr[1]/td[1]/div/img""")
    img = img1.get_attribute("src")

    my_string = personName
    splitted = my_string.split()

    first = splitted[0]
    second = splitted[1]
    third = splitted[2]

    name = (first + ' ' + second)
    personEmail = (firstName + '.' + lastName + "@fwcd.com")

    embed = discord.Embed(title=personName)
    embed.set_thumbnail(url=img)
    embed.add_field(name=personEmail, value='(email right ~70% of the time)', inline=True)

    await ctx.send(embed=embed)
    driver.get("https://www.google.com/")
    driver.delete_all_cookies()


@client.command(aliases=['parents', 'profileinfo', 'parent', 'info'])
async def profile(ctx, arg1, arg2):
    driver.delete_all_cookies()
    firstName = arg1
    lastName = arg2
    driver.get("https://fwcd.myschoolapp.com/app#login")
    sleep(5)
    try:
        username = driver.find_element_by_xpath("""//*[@id="Username"]""").send_keys('bradenbaker25')
    except:
        driver.get('https://fwcd.myschoolapp.com/app/student#directory/1412')
    sleep(1)
    try:
        nextbtn = driver.find_element_by_xpath("""//*[@id="nextBtn"]""").click()
    except:
        driver.get('https://fwcd.myschoolapp.com/app/student#directory/1412')
    sleep(1)
    try:
        password = driver.find_element_by_xpath("""//*[@id="Password"]""").send_keys('Cb575757')
    except:
        driver.get('https://fwcd.myschoolapp.com/app/student#directory/1412')
    sleep(1)
    try:
        loginbtn = driver.find_element_by_xpath("""//*[@id="loginBtn"]""").click()
    except:
        driver.get('https://fwcd.myschoolapp.com/app/student#directory/1412')
    sleep(3)
    driver.get('https://fwcd.myschoolapp.com/app/student#directory/1412')
    sleep(4)
    searchbox1 = driver.find_element_by_xpath("""//*[@id="search-text-box"]""").send_keys(firstName + ' ' + lastName)
    sleep(1)
    searchbtn = driver.find_element_by_xpath("""//*[@id="search-directory-button"]""").click()
    sleep(4)
    personName = driver.find_element_by_xpath("""//*[@id="directory-items-container"]/tbody/tr/td[2]/div[2]/h3""").text
    sleep(3)
    moreInfoBtn = driver.find_element_by_xpath("/html/body/div[2]/div/div[13]/div[1]/div/div[3]/div[1]/section/div["
                                               "2]/div[2]/div[1]/div/table/tbody/tr/td[2]/div[2]/div/div[1]").click()
    sleep(2)
    firstNameXPATH = """//*[@id="additional-container-content-5446639"]/div/table/tbody/tr[1]/td/div[1]/div[2]/h4"""
    firstEmailXPATH = """//*[@id="additional-container-content-3238044"]/div/table/tbody/tr[1]/td/div[2]/p[1]/a"""
    firstPhoneXPATH = """//*[@id="additional-container-content-3238044"]/div/table/tbody/tr[1]/td/div[2]/p[2]/a"""

    secondNameXPATH = """//*[@id="additional-container-content-5446639"]/div/table/tbody/tr[2]/td/div[1]/div[2]/h4"""
    secondEmailXPATH = """//*[@id="additional-container-content-3238044"]/div/table/tbody/tr[2]/td/div[2]/p[1]/a"""
    secondPhoneXPATH = """//*[@id="additional-container-content-5446639"]/div/table/tbody/tr[2]/td/div[2]/p[2]/a"""

    a = driver.find_element_by_xpath(
        "/html/body/div[2]/div/div[13]/div[1]/div/div[3]/div[1]/section/div[2]/div[2]/div[1]/div/table/tbody/tr/td["
        "2]/div[2]/div/div[3]/div/table/tbody/tr[1]/td").text
    b = driver.find_element_by_xpath(
        "/html/body/div[2]/div/div[13]/div[1]/div/div[3]/div[1]/section/div[2]/div[2]/div[1]/div/table/tbody/tr/td["
        "2]/div[2]/div/div[3]/div/table/tbody/tr[2]/td").text

    embed = discord.Embed()
    embed.add_field(name="First Section", value=a, inline=True)
    embed.add_field(name="Second Section", value=b, inline=True)
    await ctx.send(embed=embed)

    driver.get("https://www.google.com/")
    driver.delete_all_cookies()


@client.command()
async def all(ctx, arg1, arg2):
    if driver.current_url != "https://www.google.com/":
        return False
    else:
        await ctx.send('request received, please wait...')
        driver.delete_all_cookies()
        firstName = arg1
        lastName = arg2
        driver.get("https://fwcd.myschoolapp.com/app#login")

        # username box
        try:
            username = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, """//*[@id="Username"]""")
                                               ))
            username.send_keys('bradenbaker25')
            # username = driver.find_element_by_xpath("""//*[@id="Username"]""").send_keys('bradenbaker25')
        except:
            driver.get('https://fwcd.myschoolapp.com/app/student#directory/1412')

        # next button after username
        try:
            nextbtn = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, """//*[@id="nextBtn"]""")
                                               ))
            nextbtn.click()
            # username = driver.find_element_by_xpath("""//*[@id="Username"]""").send_keys('bradenbaker25')
        except:
            driver.get('https://fwcd.myschoolapp.com/app/student#directory/1412')

        # password after next button
        try:
            password = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, """//*[@id="Password"]""")
                                               ))
            password.send_keys('Cb575757')
            # username = driver.find_element_by_xpath("""//*[@id="Username"]""").send_keys('bradenbaker25')
        except:
            driver.get('https://fwcd.myschoolapp.com/app/student#directory/1412')

        # login button after password
        try:
            loginbtn = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, """//*[@id="loginBtn"]""")
                                               ))
            loginbtn.click()
            # username = driver.find_element_by_xpath("""//*[@id="Username"]""").send_keys('bradenbaker25')
        except:
            driver.get('https://fwcd.myschoolapp.com/app/student#directory/1412')

        # get the directory
        sleep(4)
        driver.get('https://fwcd.myschoolapp.com/app/student#directory/1412')

        # searches for student
        try:
            searchbox1 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, """//*[@id="search-text-box"]""")
                                               ))
            searchbox1.send_keys(
                firstName + ' ' + lastName)
        except:
            pass

        # search button for student lookup
        try:
            searchbtn = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, """//*[@id="search-directory-button"]""")
                                               ))
            searchbtn.click()
        except:
            pass

        # gets person name
        try:
            personName1 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, """//*[@id="directory-items-container"]/tbody/tr/td[2]/div[2]/h3""")
                                               ))
            personName = personName1.text
        except:
            pass

        # click more info button
        try:
            moreInfoBtn = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, """/html/body/div[2]/div/div[13]/div[1]/div/div[3]/div[1]/section/div[2]/div[2]/div[1]/div/table/tbody/tr/td[2]/div[2]/div/div[1]""")
                                               ))
            moreInfoBtn.click()
        except:
            pass

        # wait for stuff to appear
        sleep(3)

        firstNameXPATH = """//*[@id="additional-container-content-5446639"]/div/table/tbody/tr[1]/td/div[1]/div[2]/h4"""
        firstEmailXPATH = """//*[@id="additional-container-content-3238044"]/div/table/tbody/tr[1]/td/div[2]/p[1]/a"""
        firstPhoneXPATH = """//*[@id="additional-container-content-3238044"]/div/table/tbody/tr[1]/td/div[2]/p[2]/a"""

        secondNameXPATH = """//*[@id="additional-container-content-5446639"]/div/table/tbody/tr[2]/td/div[1]/div[2]/h4"""
        secondEmailXPATH = """//*[@id="additional-container-content-3238044"]/div/table/tbody/tr[2]/td/div[2]/p[1]/a"""
        secondPhoneXPATH = """//*[@id="additional-container-content-5446639"]/div/table/tbody/tr[2]/td/div[2]/p[2]/a"""

        a = driver.find_element_by_xpath(
            """/html/body/div[2]/div/div[13]/div[1]/div/div[3]/div[1]/section/div[2]/div[2]/div[
            1]/div/table/tbody/tr/td[2]/div[2]/div/div[3]/div/table/tbody/tr[1]/td""").text
        b = driver.find_element_by_xpath(
            """/html/body/div[2]/div/div[13]/div[1]/div/div[3]/div[1]/section/div[2]/div[2]/div[
            1]/div/table/tbody/tr/td[2]/div[2]/div/div[3]/div/table/tbody/tr[2]/td""").text

        personName = driver.find_element_by_xpath(
            """//*[@id="directory-items-container"]/tbody/tr/td[2]/div[2]/h3""").text
        img1 = driver.find_element_by_xpath("""//*[@id="directory-items-container"]/tbody/tr[1]/td[1]/div/img""")
        img = img1.get_attribute("src")

        my_string = personName
        splitted = my_string.split()

        first = splitted[0]
        second = splitted[1]
        third = splitted[2]

        name = (first + ' ' + second)
        personEmail = (firstName + '.' + lastName + "@fwcd.com")

        embed = discord.Embed()
        embed.add_field(name="First Section", value=a, inline=True)
        embed.add_field(name="Second Section", value=b, inline=True)

        embed2 = discord.Embed(title=personName)
        embed2.set_thumbnail(url=img)
        embed2.add_field(name=personEmail, value='(email right ~70% of the time)', inline=True)

        await ctx.send(embed=embed2)
        msg = await ctx.send(embed=embed)
        reactions = [checkEmoji, xEmoji]
        for emoji in reactions:
            await msg.add_reaction(emoji)

        
        sleep(2)
        driver.get("https://www.google.com/")
        driver.delete_all_cookies()
        

@client.command
async def grades(ctx, fwcdUser, fwcdPass, sendToSenderOrChat):
    # sendToSenderOrChat - me=sender, chat=chat
    print(fwcdUser)
    print(fwcdPass)
    if sendToSenderOrChat == 'me':
        print('sending to sender')
    if sendToSenderOrChat == 'chat':
        print('sending to chat')
    else:
        print('else statement')


client.run(getToken())
