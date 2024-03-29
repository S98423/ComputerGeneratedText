# coding: utf-8
# Name: Suzanna (Neely) Yates
#
#


# function #1
#

import random

def createDictionary(filename):
    """
    Inputs filename
    Outputs a dictionary of the file.
    """
    f = open(filename)
    text = f.read()
    f.close()
    LoW = text.split()

    d = {}
    pw = "$"
    for nw in LoW:
        if pw not in d: 
            d[pw] = [nw]
        else:
            d[pw] += [nw]
        pw = nw
        if nw[-1] in ".!?":
            pw = "$"
    return d

# function #2
#
def generateText(d, N):
    """
    Inputs the dictionary and number of words. 
    Outputs the text.
    """
    first_word = random.choice(d["$"])
    result = first_word
    word = first_word
    for i in range(N-1):
        if word[-1] in ".!?": 
            word = random.choice(d["$"])
            result += " " + word
        else:
            word = random.choice(d[word]) 
            result += " " + word
    return result



# CS essay:
#
"""
Bill of Rights by the Founding Fathers (Original)
Congress of the United States begun and held at the City of New-York, on Wednesday the fourth of March, one thousand seven hundred and eighty nine. THE Conventions of a number of the States, having at the time of their adopting the Constitution, expressed a desire, in order to prevent misconstruction or abuse of its powers, that further declaratory and restrictive clauses should be added: And as extending the ground of public confidence in the Government, will best ensure the beneficent ends of its institution. RESOLVED by the Senate and House of Representatives of the United States of America, in Congress assembled, two thirds of both Houses concurring, that the following Articles be proposed to the Legislatures of the several States, as amendments to the Constitution of the United States, all, or any of which Articles, when ratified by three fourths of the said Legislatures, to be valid to all intents and purposes, as part of the said Constitution; viz. ARTICLES in addition to, and Amendment of the Constitution of the United States of America, proposed by Congress, and ratified by the Legislatures of the several States, pursuant to the fifth Article of the original Constitution. Article the first... After the first enumeration required by the first article of the Constitution, there shall be one Representative for every thirty thousand, until the number shall amount to one hundred, after which the proportion shall be so regulated by Congress, that there shall be not less than one hundred Representatives, nor less than one Representative for every forty thousand persons, until the number of Representatives shall amount to two hundred; after which the proportion shall be so regulated by Congress, that there shall not be less than two hundred Representatives, nor more than one Representative for every fifty thousand persons. Article the second... No law, varying the compensation for the services of the Senators and Representatives, shall take effect, until an election of Representatives shall have intervened. Article the third... Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the Government for a redress of grievances. Article the fourth... A well regulated Militia, being necessary to the security of a free State, the right of the people to keep and bear Arms, shall not be infringed. Article the fifth... No Soldier shall, in time of peace be quartered in any house, without the consent of the Owner, nor in time of war, but in a manner to be prescribed by law. Article the sixth... The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized. Article the seventh... No person shall be held to answer for a capital, or otherwise infamous crime, unless on a presentment or indictment of a Grand Jury, except in cases arising in the land or naval forces, or in the Militia, when in actual service in time of War or public danger; nor shall any person be subject for the same offence to be twice put in jeopardy of life or limb; nor shall be compelled in any criminal case to be a witness against himself, nor be deprived of life, liberty, or property, without due process of law; nor shall private property be taken for public use, without just compensation. Article the eighth... In all criminal prosecutions, the accused shall enjoy the right to a speedy and public trial, by an impartial jury of the State and district wherein the crime shall have been committed, which district shall have been previously ascertained by law, and to be informed of the nature and cause of the accusation; to be confronted with the witnesses against him; to have compulsory process for obtaining witnesses in his favor, and to have the Assistance of Counsel for his defence. Article the ninth... In suits at common law, where the value in controversy shall exceed twenty dollars, the right of trial by jury shall be preserved, and no fact tried by a jury, shall be otherwise re-examined in any Court of the United States, than according to the rules of the common law. Article the tenth... Excessive bail shall not be required, nor excessive fines imposed, nor cruel and unusual punishments inflicted. Article the eleventh... The enumeration in the Constitution, of certain rights, shall not be construed to deny or disparage others retained by the people. Article the twelfth... The powers not delegated to the United States by the Constitution, nor prohibited by it to the States, are reserved to the States respectively, or to the people.

Bill of Rights by My Computer
'After the same offence to have the time of both Houses concurring, that there shall exceed twenty dollars, the Assistance of the said Constitution; viz. The powers not less than one Representative for every fifty thousand persons, houses, papers, and House of the Militia, when in actual service in time of the people to have been previously ascertained by Congress, that further declaratory and to be infringed. The powers not be secure in his defence. The right of religion, or prohibiting the ground of Counsel for the right of life or in time of the Senate and Amendment of public use, without due process for his defence. RESOLVED by the Senate and unusual punishments inflicted. Article the proportion shall be one hundred, after which the several States, as amendments to two thirds of Counsel for the following Articles be one Representative for public trial, by a capital, or property, without the City of March, one Representative for the proportion shall issue, but upon probable cause, supported by the right of the State and eighty nine. THE Conventions of the Legislatures of the press; or abridging the sixth... THE Conventions of the several States, having at common law, and cause of the common law, and unusual punishments inflicted. No Soldier shall, in a desire, in the freedom of America, proposed by it to the eighth... No law, where the Constitution of a witness against unreasonable searches and district shall be less than one hundred Representatives, nor shall have been committed, which Articles, when in the Militia, when ratified by the beneficent ends of the second... In suits at the several States, pursuant to the security of the people peaceably to the ninth... No Soldier shall, in the same offence to the people to a jury, shall make no law respecting an establishment of both Houses concurring, that there shall have been previously ascertained by three fourths of the persons or in any house, without dueprocess of the State and Amendment of life or naval forces, or prohibiting the Legislatures of speech, or things to be valid to the Government, will best ensure the proportion shall amount to have been previously ascertained by the seventh... Article the eighth... Article the United States of Representatives of the Constitution, expressed a number of the States of Representatives shall be twice put in actual service in order to answer for the compensation for every thirty thousand, until the fifth... The right of certain rights, shall make no Warrantsshall make no Warrants shall amount to be preserved, and to the twelfth... Article of the freedom of the seventh... The right to be confronted with the Owner, nor less than according tothe first... Article the compensation for the eleventh... In suits at common law. A well regulated Militia, being necessary to the ninth... In suits at the Government for his favor, andeighty nine. Article the rules of the City of March, one hundred, after which district wherein the States, all, or abridging the'

Pitzer Core Values by My Computer
'Our community thrives within the world through an academically rigorous, interdisciplinary liberal arts education emphasizing social opportunities. The meaningful participation of the world through an unsurpassed breadth of academic, athletic and social justice, intercultural understanding and academic program design is a Pitzer core value. Our community thrives within the world through an academically rigorous, interdisciplinary liberal arts education emphasizing social justice, intercultural understanding and academic program design is a Pitzer College produces engaged, socially responsible citizens of students, faculty and environmental sensitivity. Our community thrives within the world through an academically rigorous, interdisciplinary liberal arts education emphasizing social justice, intercultural understanding and academic program design is a Pitzer College produces engaged, socially responsible citizens of academic, athletic and social opportunities. The Claremont Colleges, which provide an unsurpassed breadth of The Claremont Colleges, which provide an academically rigorous, interdisciplinary liberal arts education emphasizing social opportunities. Our community thrives within the world through an academically rigorous, interdisciplinary liberal arts education emphasizing social opportunities. The Claremont Colleges, which provide an academically rigorous, interdisciplinary liberal arts education emphasizing social opportunities. Pitzer core value. Our community thrives within the mutually supportive framework ofacademic, athletic and environmental sensitivity. Our community thrives within the mutually supportive'
"""
#
#