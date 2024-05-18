import {useCallback, useState} from "react";
import {useNavigate} from "react-router-dom";
import styles from "./SignUp.module.css";
import HabrolinkerHeader from "../components/HabrolinkerHeader";
import HabrolinkerTextField from "../components/HabrolinkerTextField";
import HabrolinkerPasswordFields from "../components/HabrolinkerPasswordFields";
import HabrolinkerEnumField from "../components/HabrolinkerEnumField";
import HabrolinkerDateField from "../components/HabrolinkerDateField";
import HabrolinkerNumberField from "../components/HabrolinkerNumberField";
import HabrolinkerTextArrayField from "../components/HabrolinkerTextArrayField";
import {AuthenticateOnBack, SendToBackend, SendToBackendAuthorized} from "../utils";

const SignUp = () => {
    const navigate = useNavigate();

    const [registration, setRegistration] = useState({});

    const onRegister = useCallback(() => {
        console.log(registration);
        async function doRegister()
        {
            console.log(registration)
            let registerUser = await SendToBackend("POST", "/user/signup", {
                login: registration.login,
                password: registration.password
            });

            if (registerUser == null)
                alert("User with such login is already present in database");
            else
            {
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

        // check all fields
        if (registration.login == "" || registration.login == null)
            alert("Missing login");
        else if (registration.password == "" || registration.password == null)
            alert("Missing password");
        else if (registration.fullname == "" || registration.fullname == null)
            alert("Missing fullname");
        else
        {
            doRegister()
        }
    }, [navigate, registration]);

    const genderEnum = ["Женщина", "Мужчина"]


    function onLogin(data){ setRegistration((previousInfo) => ({...previousInfo, login: data}))}
    function onAvatar(data){ setRegistration((previousInfo) => ({...previousInfo, avatar: data}))}
    function onPassword(data){ setRegistration((previousInfo) => ({...previousInfo, password: data}))}
    function onFullname(data){ setRegistration((previousInfo) => ({...previousInfo, fullname: data}))}
    function onGender(data){ setRegistration((previousInfo) => ({...previousInfo, gender: data}))}
    function onBDay(data){ setRegistration((previousInfo) => ({...previousInfo, birthday: data}))}
    function onLocCountry(data){ setRegistration((previousInfo) => ({...previousInfo, location_country: data}))}
    function onLocRegion(data){ setRegistration((previousInfo) => ({...previousInfo, location_region: data}))}
    function onLocCity(data){ setRegistration((previousInfo) => ({...previousInfo, location_city: data}))}
    function onSalary(data){ setRegistration((previousInfo) => ({...previousInfo, salary: data}))}
    function onSpeciality(data){ setRegistration((previousInfo) => ({...previousInfo, speciality: data}))}
    function onSkill(data){ setRegistration((previousInfo) => ({...previousInfo, skill: data}))}

    return (
        <div className={styles.signup}>
            <HabrolinkerHeader/>
            <div className={styles.signupPage}>
                <div className={styles.userInfo}>
                    <div className={styles.div}>
                        <div className={styles.topPart}>
                            <div className={styles.div1}>
                                <b className={styles.b}>Создание аккаунта</b>
                            </div>
                            {
                                registration.avatar == null || registration.avatar == ""
                                    ? <img className={styles.avatarIcon} alt="" src="/avatar.svg"/>
                                    : <img className={styles.avatarIcon} alt="" src={registration.avatar}/>
                            }
                        </div>
                        <HabrolinkerTextField label="Логин" placeholder="some@mail.com" onChangeValue={onLogin}/>
                        <HabrolinkerTextField label="Ссылка на аватар"
                                              placeholder="http://sm.ign.com/ign_nordic/cover/a/avatar-gen/avatar-generations_prsz.jpg" onChangeValue={onAvatar}/>
                        <HabrolinkerPasswordFields label1="Пароль" label2="Повторите пароль" onChangeValue={onPassword}/>
                        <HabrolinkerTextField label="Полное имя" placeholder="Полное имя" onChangeValue={onFullname}/>
                        <HabrolinkerEnumField label="Пол" enumeration={genderEnum} value={1} onChangeValue={onGender}/>
                        <HabrolinkerDateField label="Дата рождения" onChangeValue={onBDay}/>
                        <HabrolinkerTextField label="Страна" placeholder="Страна" onChangeValue={onLocCountry}/>
                        <HabrolinkerTextField label="Район" placeholder="Район" onChangeValue={onLocRegion}/>
                        <HabrolinkerTextField label="Город" placeholder="Город" onChangeValue={onLocCity}/>
                        <HabrolinkerNumberField label="Доход (в долларах)" value={1000} onChangeValue={onSalary}/>
                        <HabrolinkerTextArrayField label="Cпециальности"
                                                   placeholder={["Fullstack Developer", "Game Developer"]}
                                                   onChangeValue={onSpeciality}
                        />
                        <HabrolinkerTextArrayField label="Навыки" placeholder={["С++", "Python", "Git"]} onChangeValue={onSkill}/>
                    </div>
                    <div className={styles.controllPart}>
                        <div className={styles.createButton} onClick={onRegister}>
                            <b>Создать аккаунт</b>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default SignUp;
