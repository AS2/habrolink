import styles from "./HabrolinkerUserCard.module.css";
import {useCallback, useEffect, useState} from "react";
import {HasToken, SendToBackend, SendToBackendAuthorized} from "../utils";
import {BACKEND_INVALID_PERSON_ID, DEFAULT_AVATAR} from "../config";
import {useNavigate} from "react-router-dom";

const HabrolinkerUserCard = ({personId}) => {
    const navigate = useNavigate();

    const [info, setInfo] = useState({
        hasPerson: false,
        hasUser: false,
        avatar: DEFAULT_AVATAR,
        isMarked: false,
        fullname: "",

    });

    useEffect(() => {
        async function fetchData() {
            let personInfo = await SendToBackend("POST", "/person/info", {person_id: personId});
            if (personInfo != null) {
                setInfo((oldInfo) => ({
                    ...oldInfo,
                    hasPerson: true,
                    avatar: personInfo.avatar == "" ? DEFAULT_AVATAR : personInfo.avatar,
                    fullname: personInfo.fullname == "" ? personInfo.id : personInfo.fullname,
                    id: personInfo.id,
                    source: personInfo.source,
                    habr_karma: personInfo.habr_karma,
                    habr_rating: personInfo.habr_rating
                }))

                let userId = await SendToBackend("POST", "/user/find", {person_id: personId});
                if (userId != null) {
                    let userInfo = await SendToBackend("POST", "/user/info", {user_id: userId.user_id});
                    if (userInfo != null) {
                        setInfo((oldInfo) => ({
                            ...oldInfo,
                            hasUser: true,
                            userId: userId,
                            login: userInfo.login
                        }))
                    }
                }

                let isMarked = await SendToBackendAuthorized("POST", "/mark/status", {person_id: personId});
                if (isMarked != null) {
                    setInfo((oldInfo) => ({
                        ...oldInfo,
                        isMarked: isMarked.status
                    }))
                }
            }
        }

        fetchData()
    }, []);

    const onSendMessage = useCallback(() => {
        const params = new URLSearchParams({
            chatId: info.userId
        });

        navigate("/chats-page?" + params.toString());
    }, [navigate, info]);

    const onMark = useCallback(() => {
        async function fetchData() {
            if (info.isMarked) {
                await SendToBackendAuthorized("DELETE", "/mark/remove", {person_id: personId});
            } else {
                await SendToBackendAuthorized("PUT", "/mark/add", {person_id: personId});
            }
            setInfo((oldInfo) => ({
                ...oldInfo,
                isMarked: !info.isMarked
            }))
        }

        fetchData()
    }, [info]);

    const onInfo = useCallback(() => {
    }, [info]);

    return (
        <div className={styles.userCard}>
            <div className={styles.mainInfo}>
                <img className={styles.avatarIcon} alt="" src={info.avatar}/>
                <div className={styles.description}>
                    <b className={styles.fullname}>{info.fullname}</b>
                    {(info.hasPerson && info.source == 1)
                        ? <div className={styles.habrInfo}>
                            <a href={"https://habr.com/ru/users/" + info.id}>@{info.id}</a>
                            <div className={styles.dot}>●</div>
                            Карма: {info.habr_karma}
                            <div className={styles.dot}>●</div>
                            Рейтинг: {info.habr_rating}
                        </div>
                        : <div className={styles.habrInfo}>
                            -Не привязан аккаунт Хабрахабр-
                        </div>
                    }
                    {info.hasUser
                        ? (<div className={styles.habrInfo}>
                            Логин ХаброЛинкер:
                            <div className={styles.email}>
                            {info.login}
                        </div>
                        </div>)
                        : <div className={styles.habrInfo}>
                            -Не привязан аккаунт ХаброЛинкер-
                        </div>
                    }

                </div>
            </div>
            <div className={styles.actionsButtons}>
                {HasToken() && info.hasUser &&
                    <div className={styles.buttonDiv} onClick={onSendMessage}>
                        <img
                            className={styles.buttonIcon}
                            alt=""
                            src="/habrolinker-icon-chat.svg"
                        />
                    </div>
                }
                {HasToken() &&
                    <div className={styles.buttonDiv} onClick={onMark}>
                        <img
                            className={styles.buttonIcon}
                            alt=""
                            src={info.isMarked ? "/habrolinker-icon-marked.svg" : "/habrolinker-icon-unmarked.svg"}
                        />
                    </div>
                }
                {false && <div className={styles.buttonDiv} onClick={onInfo}>
                    <img
                        className={styles.buttonIcon}
                        alt=""
                        src="/habrolinker-icon-info.svg"
                    />
                </div>}
            </div>
        </div>
    );
};

export default HabrolinkerUserCard;
