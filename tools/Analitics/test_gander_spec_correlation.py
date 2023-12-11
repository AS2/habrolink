import psycopg
from matplotlib import pyplot as plt
import numpy as np
import datetime


DB_NAME = "########"
DB_USER = "########"
DB_PASSWORD = "########"

conn = psycopg.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD)


def LoadQuery(fileName):
    return open(f"tools/Queries/{fileName}.sql", "r").read()


specGroups = {
    "Design & Creativity": [
        "UI/UX Designer",
        "Web Designer",
        "Product Designer",
        "Graphic Designer",
        "Motion Designer",
        "Designer Illustrator",
        "3d Modeler",
        "3d Animator",
        "Art Director",
        "Application Designer",
        "Narrative Designer",
        "Content Manager",
        "Flash Animator",
        "VUI-designer",
        "Computer Graphics Artist"
    ],
    "Game Development": [
        "Game Developer",
        "Game Designer",
    ],
    "Software Development": [
        "Frontend Developer",
        "Backend Developer",
        "Fullstack Developer",
        "System Software Engineer",
        "Embedded Software Engineer",
        "Software Developer",
        "Mobile Application Developer",
        "Application Developer",
        "Database Developer",
        "1C Developer",
        "ERP Developer",
        "Web Developer",
        "Software Architect",
        "HTML Coding"
    ],
    "Technical Support & IT Operations": [
        "System Administration",
        "Server Administrator",
        "Technical Support Analyst",
        "Technical Support Manager",
        "Technical Support Engineer",
        "Technical Support Director",
        "Site Administrator",
        "DevOps",
        "Site Reliability Engineer (SRE)",
        "Zerocoder",
        "Release Manager"
    ],
    "Quality Assurance & Testing": [
        "Quality Assurance Engineer",
        "Manual Test Engineer",
        "Quality Assurance Manager",
        "Quality Assurance Director",
        "UX Tester",
        "Test Automation Engineer",
        "Software Performance Engineer",
        "Quality Assurance Analyst"
    ],
    "Network & Security": [
        "Network Engineer",
        "Security Administrator",
        "Pentester",
        "Security Engineer",
        "Инженер по безопасности"
    ],
    "Data Management & Analysis": [
        "Data Analyst",
        "ML Engineer",
        "Data Scientist",
        "Data Engineer",
        "BI Developer",
        "Web Analyst",
        "Marketing Analyst",
        "Antifraud Analyst",
        "Sales Analyst",
        "Mobile Analyst",
        "Game Analyst",
        "Database Architect",
        "Database Administrator",
        "MLOps",
        "Специалист по реверс-инжинирингу",
        "Software Analyst",
        "Reverse Engineer",
        "Quality Assurance Analyst"
    ],
    "Management & Executive Leadership": [
        "Chief Executive Officer (CEO)",
        "Project Manager",
        "Project Director",
        "Product Manager",
        "Chief Product Officer (CPO)",
        "Program Manager",
        "Product Analyst",
        "Chief information officer (CIO)",
        "Chief Technology Officer (CTO)",
        "Chief Financial Officer (CFO)",
        "Chief Operating Officer (COO)",
        "Account Director",
        "Content Director",
        "Sales Director",
        "Customer Service Director",
        "HR Director",
        "Recruitment Director",
        "Customer Service Manager",
        "Scrum Master",
        "Marketing Manager"
    ],
    "Business & Market Analysis": [
        "Systems Analyst",
        "Business Analyst"
    ],
    "Marketing & Public Relations": [
        "Marketing Director",
        "Sales manager",
        "Account Manager",
        "Content Manager",
        "Targetologist",
        "SEO Specialist",
        "PPC specialist",
        "PR-manager",
        "Community manager",
        "SMM Specialist",
        "Directologist",
        "DevRel",
        "Marketing Manager"
    ],
    "Content & Writing": [
        "Content Manager",
        "Content Writer",
        "Copywriter",
        "Technical Writer",
        "HR Brand Development Manager"
    ],
    "HR & Recruitment": [
        "Recruitment Manager",
        "HR Manager",
        "HR Analyst",
        "Personnel Training and Development Manager"
    ],
    "Administration & Support": [
        "Office Manager",
        "Moderator"
    ],
    "Legal Affairs": [
        "Lawyer"
    ],
    "Finance & Accounting": [
        "Accountant"
    ],
    "Other": [
        "Other"
    ]
}

def test_gender_spec_correlation(capsys):
    specializationAndGender = LoadQuery("rawDataSpecializationAndGender")
    width = 0.9
    with capsys.disabled():
        with conn.cursor() as cur:
            cur.execute(specializationAndGender)
            specList = []
            noneDict = {}
            maleDict = {}
            femaleDict = {}
            totalDict = {}
            res = cur.fetchone()
            while res:
                spec = res[0]
                specList.append(spec)
                noneDict[spec] = 0
                maleDict[spec] = 0
                femaleDict[spec] = 0
                while res and res[0] == spec:
                    if res[1] == 0:
                        noneDict[spec] = res[2]
                    elif res[1] == 1:
                        maleDict[spec] = res[2]
                    elif res[1] == 2:
                        femaleDict[spec] = res[2]
                    res = cur.fetchone()
                totalDict[spec] = noneDict[spec] + maleDict[spec] + femaleDict[spec]
            specListSorted = sorted(specList, key=lambda x: totalDict[x], reverse=True)
            total = 0
            for spec in specListSorted:
                total += totalDict[spec]
            other = 0
            specListPie = []
            for spec in specListSorted:
                if spec == "Other" or totalDict[spec] / total < 0.015:
                    other += totalDict[spec]
                else:
                    specListPie.append(spec)
            totalListPie = [totalDict[x] for x in specListPie]
            totalListPie.append(other)
            specListPie.append("Other")
            fig, ax1 = plt.subplots()
            ax1.pie(totalListPie, labels=specListPie)
            plt.savefig(fname=f"./pics/analitics/spec_pie.png", bbox_inches='tight', dpi=200)
            for name, order in zip(["female", "male"],[femaleDict, maleDict]):
                fig, ax1 = plt.subplots()
                specListSorted = sorted(specList, key=lambda x: order[x] and order[x]/(maleDict[x] + femaleDict[x]) or 0, reverse=True)
                specListFiltered = []
                for spec in specListSorted:
                    if maleDict[spec] + femaleDict[spec] >= 50:
                        specListFiltered.append(spec)
                noneList = np.array([noneDict[spec] for spec in specListFiltered])
                maleList = np.array([maleDict[spec] for spec in specListFiltered])
                femaleList = np.array([femaleDict[spec] for spec in specListFiltered])
                totalList = np.array([maleDict[spec] + femaleDict[spec] for spec in specListFiltered])
                topk = 10
                plt.xticks(rotation=90)
                bottom = np.zeros(topk)
                p = ax1.bar(specListFiltered[:topk], maleList[:topk]/totalList[:topk], width, label="Male", bottom=bottom)
                ax1.bar_label(p, labels=maleList[:topk], label_type='center')
                bottom += maleList[:topk]/totalList[:topk]
                p = ax1.bar(specListFiltered[:topk], femaleList[:topk]/totalList[:topk], width, label="Female", bottom=bottom)
                ax1.bar_label(p, labels=femaleList[:topk], label_type='center')
                bottom += femaleList[:topk]/totalList[:topk]
                p = ax1.bar(specListFiltered[:topk], noneList[:topk]/totalList[:topk], width, label="None", bottom=bottom)
                ax1.bar_label(p, labels=noneList[:topk], label_type='center')
                bottom += noneList[:topk]/totalList[:topk]
                ax1.label_outer()
                ax1.legend()
                plt.savefig(fname=f"./pics/analitics/top_{name}_gender_spec.png", bbox_inches='tight', dpi=200)


def test_gender_spec_classes_correlation(capsys):
    specializationAndGender = LoadQuery("rawDataSpecializationAndGender")
    width = 0.9
    with capsys.disabled():
        with conn.cursor() as cur:
            cur.execute(specializationAndGender)
            groupList = []
            noneDict = {}
            maleDict = {}
            femaleDict = {}
            totalDict = {}
            res = cur.fetchone()
            while res:
                spec = res[0]
                groups = []
                for gr, specList in specGroups.items():
                    if spec in specList:
                        groups.append(gr)
                for group in groups:
                    if group not in groupList:
                        groupList.append(group)
                        noneDict[group] = 0
                        maleDict[group] = 0
                        femaleDict[group] = 0
                        totalDict[group] = 0
                while res and res[0] == spec:
                    for group in groups:
                        if res[1] == 0:
                            noneDict[group] += res[2]
                        elif res[1] == 1:
                            maleDict[group] += res[2]
                        elif res[1] == 2:
                            femaleDict[group] += res[2]
                        totalDict[group] += res[2]
                    res = cur.fetchone()
            groupListSorted = sorted(groupList, key=lambda x: totalDict[x], reverse=True)
            total = 0
            for group in groupListSorted:
                total += totalDict[group]
            other = 0
            groupListPie = []
            for group in groupListSorted:
                if group == "Other" or totalDict[group] / total < 0.01:
                    other += totalDict[group]
                else:
                    groupListPie.append(group)
            totalListPie = [totalDict[x] for x in groupListPie]
            totalListPie.append(other)
            groupListPie.append("Other")
            fig, ax1 = plt.subplots()
            ax1.pie(totalListPie, labels=groupListPie)
            plt.savefig(fname=f"./pics/analitics/spec_groups_pie.png", bbox_inches='tight', dpi=200)

            fig, ax1 = plt.subplots()
            groupListSorted = sorted(groupList, key=lambda x: femaleDict[x] and femaleDict[x]/(maleDict[x] + femaleDict[x]) or 0, reverse=True)
            groupListFiltered = []
            for group in groupListSorted:
                if maleDict[group] + femaleDict[group] >= 50:
                    groupListFiltered.append(group)
            noneList = np.array([noneDict[group] for group in groupListFiltered])
            maleList = np.array([maleDict[group] for group in groupListFiltered])
            femaleList = np.array([femaleDict[group] for group in groupListFiltered])
            totalList = np.array([maleDict[group] + femaleDict[group] for group in groupListFiltered])
            topk = len(groupListFiltered)
            plt.xticks(rotation=90)
            bottom = np.zeros(topk)
            p = ax1.bar(groupListFiltered[:topk], maleList[:topk]/totalList[:topk], width, label="Male", bottom=bottom)
            ax1.bar_label(p, labels=maleList[:topk], label_type='center')
            bottom += maleList[:topk]/totalList[:topk]
            p = ax1.bar(groupListFiltered[:topk], femaleList[:topk]/totalList[:topk], width, label="Female", bottom=bottom)
            ax1.bar_label(p, labels=femaleList[:topk], label_type='center')
            bottom += femaleList[:topk]/totalList[:topk]
            p = ax1.bar(groupListFiltered[:topk], noneList[:topk]/totalList[:topk], width, label="None", bottom=bottom)
            ax1.bar_label(p, labels=noneList[:topk], label_type='center')
            bottom += noneList[:topk]/totalList[:topk]
            ax1.label_outer()
            ax1.legend()
            plt.savefig(fname=f"./pics/analitics/top_female_gender_spec_groups.png", bbox_inches='tight', dpi=200)
