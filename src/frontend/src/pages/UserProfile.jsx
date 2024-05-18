import {useCallback, useEffect, useState} from "react";
import {useNavigate} from "react-router-dom";
import HabrolinkerHeader from "../components/HabrolinkerHeader";
import styles from "./UserProfile.module.css";
import {RemoveToken, SendToBackend, SendToBackendAuthorized} from "../utils";
import {BACKEND_INVALID_PERSON_ID, DEFAULT_AVATAR} from "../config";

const UserProfile = () => {
    const navigate = useNavigate();

    const [info, setInfo] = useState({
        hasUser: false,
        hasPerson: false
    });

    const onRedactClick = useCallback(() => {
        navigate("/user-profile-edit");
    }, [navigate]);

    async function GetUserInfo() {
        const userInfo = await SendToBackendAuthorized("POST", "/user/self", {})
        if (userInfo == null) {
            RemoveToken()
            navigate("/")
        } else {
            setInfo((previousInfo) => ({
                ...previousInfo,
                login: userInfo["login"],
                hasUser: true
            }))

            if (userInfo["person_id"] == BACKEND_INVALID_PERSON_ID) {
                setInfo((previousInfo) => ({
                    ...previousInfo,
                    has_person: false
                }))
            } else {
                const personInfo = await SendToBackend("POST", "/person/info", {"person_id": userInfo["person_id"]})
                if (personInfo == null) {
                    setInfo((previousInfo) => ({
                        ...previousInfo,
                        has_person: false
                    }))
                } else {
                    setInfo((previousInfo) => ({
                        ...previousInfo,
                        hasPerson: true,
                        fullname: personInfo["fullname"],
                        avatar: personInfo["avatar"],
                        person_id: personInfo["id"],
                        source: personInfo["source"],
                        gender: personInfo["gender"],
                        birthday: personInfo["birthday"],
                        location_country: personInfo["location_country"],
                        location_city: personInfo["location_city"],
                        location_region: personInfo["location_region"],
                        salary: personInfo["salary"],
                        habr_rating: personInfo["habr_rating"],
                        habr_karma: personInfo["habr_karma"],
                        specialities: personInfo["specialities"],
                        skills: personInfo["skills"]
                    }))
                }
            }
        }
    }

    useEffect(() => {
        GetUserInfo()
    }, [navigate]);

    return (
        <div className={styles.userProfile}>
            <HabrolinkerHeader/>
            <div className={styles.userInfo}>
                <b className={styles.header1}>Аккаунт ХаброЛинкер</b>
                {
                    info.hasUser &&
                    <div className={styles.topPart}>
                        <div className={styles.textPart}>
                            <b className={styles.header2}>Основная информация</b>
                            <div className={styles.fieldsText}>
                                <div className={styles.line}>
                                    <span>{`Логин: `}</span>
                                    <b>{info.login}</b>
                                </div>
                                <div className={styles.line}>
                                    <span>{`Имя: `}</span>
                                    <b>{info.fullname == "" ? "Не указано" : info.fullname}</b>
                                </div>
                                <div className={styles.line}>
                                    <span>{`Habr аккаунт: `}</span>
                                    {
                                        (info.hasPerson && info.source === 1)
                                            ? <b> {info.person_id} </b>
                                            : <b> Не привязан </b>
                                    }
                                </div>
                            </div>
                        </div>
                        {
                            info.hasPerson
                                ? <img className={styles.avatarIcon} alt="" src={info.avatar}/>
                                : <img className={styles.avatarIcon} alt="" src={DEFAULT_AVATAR}/>
                        }
                    </div>
                }
                {
                    info.hasPerson &&
                    <div className={styles.bottomPart}>
                        <div className={styles.textPart}>
                            <b className={styles.header2}>Дополнительная информация</b>
                            <div className={styles.fieldsText}>
                                <div className={styles.line}>{"Пол: "}
                                    {
                                        info.gender === 1
                                            ? <b>Мужчина</b> :
                                            <b>Женщина</b>}
                                </div>
                                <div className={styles.line}>
                                    <span>{`Дата рождения: `}</span>
                                    <b>{info.birthday == "" ? "Не указано" : info.birthday}</b>
                                </div>
                                <div className={styles.line}>
                                    <span>{`Страна: `}</span>
                                    <b>{info.location_country == "" ? "Не указано" : info.location_country}</b>
                                </div>
                                <div className={styles.line}>
                                    <span>{`Регион: `}</span>
                                    <b>{info.location_region == "" ? "Не указано" : info.location_region}</b>
                                </div>
                                <div className={styles.line}>
                                    <span>{`Город: `}</span>
                                    <b>{info.location_city == "" ? "Не указано" : info.location_city}</b>
                                </div>
                                <div className={styles.line}>
                                    <span>{`Указанный доход: `}</span>
                                    <b>{info.salary === null ? "Не указано" : info.salary + "$"}</b>
                                </div>
                                {info.source === 1 &&
                                    <div className={styles.line}>
                                        <span>{`Рейтинг Хабра: `}</span>
                                        <b>{info.habr_rating}</b>
                                    </div>
                                }
                                {info.source === 1 &&
                                    <div className={styles.line}>
                                        <span>{`Карма Хабра: `}</span>
                                        <b>{info.habr_karma}</b>
                                    </div>
                                }
                                <div className={styles.line}>
                                    <span>{`Специальности: `}</span>
                                    {info.specialities.length > 0
                                        ? <b>{ info.specialities.map((el, i) => el + ", ")}</b>
                                        : <b>Не указано</b>}
                                </div>
                                <div className={styles.line}>
                                    <span>{`Умения: `}</span>
                                    {info.skills.length > 0
                                        ? <b>{ info.skills.map((el, i) => el + ", ")}</b>
                                        : <b>Не указано</b>}
                                </div>
                            </div>
                        </div>
                    </div>
                }
                <div className={styles.redactButton} onClick={onRedactClick}>
                    Редактировать
                </div>
            </div>
        </div>
    );
};

export default UserProfile;
