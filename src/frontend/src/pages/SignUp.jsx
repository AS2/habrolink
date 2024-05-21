import { useCallback, useState } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./SignUp.module.css";
import Form from "react-bootstrap/Form";
import HabrolinkerHeader from "../components/HabrolinkerHeader";
import HabrolinkerTextField from "../components/HabrolinkerTextField";
import HabrolinkerPasswordFields from "../components/HabrolinkerPasswordFields";
import HabrolinkerEnumField from "../components/HabrolinkerEnumField";
import HabrolinkerDateField from "../components/HabrolinkerDateField";
import HabrolinkerNumberField from "../components/HabrolinkerNumberField";
import HabrolinkerTextArrayField from "../components/HabrolinkerTextArrayField";
import { AuthenticateOnBack, SendToBackend, SendToBackendAuthorized } from "../utils";
import { DEFAULT_AVATAR } from "../config";

const SignUp = () => {
    const navigate = useNavigate();

    const [registration, setRegistration] = useState({});
    const [isLinking, setLinking] = useState(false)

    const onRegister = useCallback(() => {
        async function doRegister() {
            let registerUser = await SendToBackend("POST", "/user/signup", {
                login: registration.login,
                password: registration.password
            });

            if (registerUser == null)
                alert("User with such login is already present in database");
            else {
                AuthenticateOnBack(registration.login, registration.password)
                SendToBackendAuthorized("POST", "/person/create", {
                    fullname: registration.fullname,
                    avatar: registration.avatar,
                    gender: registration.gender,
                    birthday: registration.birthday,
                    location_country: registration.location_country,
                    location_region: registration.location_region,
                    location_city: registration.location_city,
                    salary: registration.salary,
                    specialities: registration.specialities,
                    skills: registration.skills
                });
                navigate("/");
            }
        }

        async function doLink() {
            // find person
            let personInfo = await SendToBackend("POST", "/person/info", {
                person_id: registration.habr_login
            });

            if (personInfo == null)
                alert("Unknown habr account")
            else {
                let checkPerson = await SendToBackend("POST", "/user/find", {
                    person_id: registration.habr_login
                });
                if (checkPerson != null)
                    alert("This habr account is already linked to another user")
                else {
                    let registerUser = await SendToBackend("POST", "/user/signup", {
                        login: registration.login,
                        password: registration.password
                    });
                    if (registerUser == null)
                        alert("User with such login is already present in database");
                    else {
                        await AuthenticateOnBack(registration.login, registration.password)
                        await SendToBackendAuthorized("POST", "/person/link", {
                            person_id: registration.habr_login
                        });
                        navigate("/");
                    }
                }
            }
        }

        // check all fields
        if (registration.login == "" || registration.login == null)
            alert("Missing login");
        else if (registration.password == "" || registration.password == null)
            alert("Missing password");
        else if (isLinking == false && (registration.fullname == "" || registration.fullname == null))
            alert("Missing fullname");
        else if (isLinking == true && (registration.habr_login == "" || registration.habr_login == null))
            alert("Missing Habr login");
        else {
            if (isLinking)
                doLink()
            else
                doRegister()
        }
    }, [navigate, registration, isLinking]);

    const genderEnum = ["Женщина", "Мужчина"]


    function onLogin(data) {
        setRegistration((previousInfo) => ({ ...previousInfo, login: data }))
    }

    function onPassword(data) {
        setRegistration((previousInfo) => ({ ...previousInfo, password: data }))
    }

    function onAvatar(data) {
        setRegistration((previousInfo) => ({ ...previousInfo, avatar: data }))
    }

    function onFullname(data) {
        setRegistration((previousInfo) => ({ ...previousInfo, fullname: data }))
    }

    function onGender(data) {
        setRegistration((previousInfo) => ({ ...previousInfo, gender: data }))
    }

    function onBDay(data) {
        setRegistration((previousInfo) => ({ ...previousInfo, birthday: data }))
    }

    function onLocCountry(data) {
        setRegistration((previousInfo) => ({ ...previousInfo, location_country: data }))
    }

    function onLocRegion(data) {
        setRegistration((previousInfo) => ({ ...previousInfo, location_region: data }))
    }

    function onLocCity(data) {
        setRegistration((previousInfo) => ({ ...previousInfo, location_city: data }))
    }

    function onSalary(data) {
        setRegistration((previousInfo) => ({ ...previousInfo, salary: data }))
    }

    function onSpeciality(data) {
        setRegistration((previousInfo) => ({ ...previousInfo, specialities: data }))
    }

    function onSkill(data) {
        setRegistration((previousInfo) => ({ ...previousInfo, skills: data }))
    }

    function onHabrLogin(data) {
        setRegistration((previousInfo) => ({ ...previousInfo, habr_login: data }))

        async function updateAvatar() {
            let person = await SendToBackend("POST", "/person/info", {
                person_id: data
            });
            if (person != null)
                setRegistration((previousInfo) => ({ ...previousInfo, avatar: person.avatar }))
            else
                setRegistration((previousInfo) => ({ ...previousInfo, avatar: null }))
        }

        updateAvatar()
    }

    function onLinkingChange() {
        setLinking((previousInfo) => (!previousInfo));
        setRegistration((previousInfo) => ({ ...previousInfo, avatar: null }))
    }

    return (
        <div className={styles.signup}>
            <HabrolinkerHeader />
            <div className={styles.signupPage}>
                <div className={styles.userInfo}>
                    <div className={styles.div}>
                        <div className={styles.topPart}>
                            <div className={styles.div1}>
                                <b>Создание аккаунта</b>
                            </div>
                            {
                                registration.avatar == null || registration.avatar == ""
                                    ? <img className={styles.avatarIcon} alt="" src={DEFAULT_AVATAR} />
                                    : <img className={styles.avatarIcon} alt="" src={registration.avatar} />
                            }
                        </div>
                        <HabrolinkerTextField label="Логин" placeholder="some@mail.com" onChangeValue={onLogin} />
                        <HabrolinkerPasswordFields label1="Пароль" label2="Повторите пароль"
                            onChangeValue={onPassword} />
                        <Form.Switch className={styles.formSwitch} id="linkSwitch" label="У меня уже есть аккаунт на Habrahabr"
                            checked={isLinking} onChange={onLinkingChange} />
                        {
                            isLinking
                                ? <div>
                                    <HabrolinkerTextField key={"habrLogin"} label="Логин на Habr" placeholder="Логин на Habr"
                                        onChangeValue={onHabrLogin} />
                                </div>
                                : <div>
                                    <HabrolinkerTextField key={"avatar"} label="Ссылка на аватар"
                                        placeholder="http://sm.ign.com/ign_nordic/cover/a/avatar-gen/avatar-generations_prsz.jpg"
                                        onChangeValue={onAvatar} />
                                    <HabrolinkerTextField key={"fullname"} label="Полное имя" placeholder="Полное имя"
                                        onChangeValue={onFullname} />
                                    <HabrolinkerEnumField key={"gender"} label="Пол" enumeration={genderEnum} value={1}
                                        onChangeValue={onGender} />
                                    <HabrolinkerDateField key={"bday"} label="Дата рождения" onChangeValue={onBDay} />
                                    <HabrolinkerTextField key={"country"} label="Страна" placeholder="Страна" onChangeValue={onLocCountry} />
                                    <HabrolinkerTextField key={"region"} label="Район" placeholder="Район" onChangeValue={onLocRegion} />
                                    <HabrolinkerTextField key={"city"} label="Город" placeholder="Город" onChangeValue={onLocCity} />
                                    <HabrolinkerNumberField key={"salary"} label="Доход (в долларах)" value={1000}
                                        onChangeValue={onSalary} />
                                    <HabrolinkerTextArrayField key={"speciality"} label="Cпециальности"
                                        placeholder={["Fullstack Developer", "Game Developer"]}
                                        onChangeValue={onSpeciality} />
                                    <HabrolinkerTextArrayField key={"skill"} label="Навыки" placeholder={["С++", "Python", "Git"]}
                                        onChangeValue={onSkill} />
                                </div>
                        }
                    </div>
                    <div className={styles.controllPart}>
                        <div className={styles.createButton} onClick={onRegister}>
                            <b>Создать аккаунт</b>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
        ;
};

export default SignUp;
