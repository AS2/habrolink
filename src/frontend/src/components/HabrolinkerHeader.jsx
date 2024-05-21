import { useCallback, useEffect, useState } from "react";
import styles from "./HabrolinkerHeader.module.css";
import { useNavigate } from "react-router-dom";
import { BACKEND_INVALID_PERSON_ID, DEFAULT_AVATAR } from "../config";
import { HasToken, RemoveToken, SendToBackend, SendToBackendAuthorized } from "../utils";

const HabrolinkerHeader = ({ }) => {
    const navigate = useNavigate();

    const [userIcon, setUserIcon] = useState(DEFAULT_AVATAR);

    const onLogoClick = useCallback(() => {
        navigate("/");
    }, []);

    const onSearchClick = useCallback(() => {
        navigate("/search-page");
    }, []);

    const onMessageClick = useCallback(() => {
        navigate("/chats-page");
    }, []);

    const onMarkedClick = useCallback(() => {
        navigate("/saved-users");
    }, []);

    const onLogoutClick = useCallback(() => {
        RemoveToken();
        navigate("/");
    }, []);

    const onProfileClick = useCallback(() => {
        navigate("/user-profile");
    }, []);

    const onLoginClick = useCallback(() => {
        navigate("/signin");
    }, []);

    useEffect(() => {
        async function fetchData() {

            let userInfo = await SendToBackendAuthorized("POST", "/user/self", {});
            if (userInfo != null && userInfo["person_id"] !== BACKEND_INVALID_PERSON_ID) {
                let personInfo = await SendToBackend("POST", "/person/info", {
                    person_id: userInfo.person_id
                });
                if (personInfo["avatar"].startsWith("http") && personInfo["avatar"] != "https://someimage.org/img.png")
                    setUserIcon(personInfo["avatar"]);
            }
        }

        if (HasToken())
            fetchData()
    }, [userIcon]);

    return (
        <div className={styles.header}>
            <b className={styles.logo} onClick={onLogoClick}>
                <span>{`{`}</span>
                <span className={styles.logoBlue}>Хабро:</span>
                <span>{`Линкер}`}</span>
            </b>


            <div className={styles.headerRight}>
                <img
                    className={styles.searchButton}
                    src="/habrolinker-icon-search.svg"
                    onClick={onSearchClick}
                />
                {HasToken() &&
                    <img
                        className={styles.markedButton}
                        src="/habrolinker-icon-marked.svg"
                        onClick={onMarkedClick}
                    />
                }
                {HasToken() &&
                    <img
                        className={styles.messagesButton}
                        src="/habrolinker-icon-chat.svg"
                        onClick={onMessageClick}
                    />
                }
                {HasToken() &&
                    <img
                        className={styles.logOutButton}
                        src="/habrolinker-icon-logout.svg"
                        onClick={onLogoutClick}
                    />
                }
                {HasToken() &&
                    <img
                        className={styles.profileButton}
                        src={userIcon}
                        onClick={onProfileClick}
                    />}

                {!HasToken() &&
                    <b className={styles.login} onClick={onLoginClick}>
                        <span className={styles.logoBlue}>Войти</span>

                    </b>}
            </div>
        </div>
    );
};

export default HabrolinkerHeader;
