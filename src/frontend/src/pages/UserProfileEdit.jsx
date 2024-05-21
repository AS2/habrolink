import { useCallback, useState, useEffect } from "react";
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
import { RemoveToken, SendToBackend, SendToBackendAuthorized } from "../utils";
import { BACKEND_INVALID_PERSON_ID, DEFAULT_AVATAR } from "../config";

const UserProfileEdit = () => {
  const navigate = useNavigate();

  const [info, setInfo] = useState({
    hasUser: false,
    hasPerson: false
  });

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
        const personInfo = await SendToBackend("POST", "/person/info", { "person_id": userInfo["person_id"] })
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
            gender: personInfo["gender"],
            birthday: personInfo["birthday"],
            location_country: personInfo["location_country"],
            location_city: personInfo["location_city"],
            location_region: personInfo["location_region"],
            salary: personInfo["salary"],
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

  const onSaveEdit = useCallback(() => {
    async function saveData() {
      let signedUser = await SendToBackendAuthorized("POST", "/user/self", {});

      if (signedUser == null) {
        alert("User isnt authenticated");
        RemoveToken()
        navigate("/")
      }
      else {
        SendToBackendAuthorized("PUT", "/person/update", {
          fullname: info.fullname,
          avatar: info.avatar,
          gender: info.gender,
          birthday: info.birthday,
          location_country: info.location_country,
          location_region: info.location_region,
          location_city: info.location_city,
          salary: info.salary,
          specialities: info.specialities,
          skills: info.skills
        });
        navigate("/user-profile");
      }
    }

    // check all fields
    if (info.fullname == "" || info.fullname == null)
      alert("Full name is empty!");
    else
      saveData()
  }, [navigate, info]);

  const genderEnum = ["Женщина", "Мужчина"]

  function onAvatar(data) {
    setInfo((previousInfo) => ({ ...previousInfo, avatar: data }))
  }

  function onFullname(data) {
    setInfo((previousInfo) => ({ ...previousInfo, fullname: data }))
  }

  function onGender(data) {
    setInfo((previousInfo) => ({ ...previousInfo, gender: data }))
  }

  function onBDay(data) {
    setInfo((previousInfo) => ({ ...previousInfo, birthday: data }))
  }

  function onLocCountry(data) {
    setInfo((previousInfo) => ({ ...previousInfo, location_country: data }))
  }

  function onLocRegion(data) {
    setInfo((previousInfo) => ({ ...previousInfo, location_region: data }))
  }

  function onLocCity(data) {
    setInfo((previousInfo) => ({ ...previousInfo, location_city: data }))
  }

  function onSalary(data) {
    setInfo((previousInfo) => ({ ...previousInfo, salary: data }))
  }

  function onSpeciality(data) {
    setInfo((previousInfo) => ({ ...previousInfo, specialities: data }))
  }

  function onSkill(data) {
    setInfo((previousInfo) => ({ ...previousInfo, skills: data }))
  }

  return (
    <div className={styles.signup}>
      <HabrolinkerHeader />
      <div className={styles.signupPage}>
        <div className={styles.userInfo}>
          <div className={styles.div}>
            <div className={styles.topPart}>
              <div className={styles.div1}>
                <b>Редактирование аккаунта</b>
              </div>
              {
                info.avatar == null || info.avatar == "" || info.avatar == "https://someimage.org/img.png"
                  ? <img className={styles.avatarIcon} alt="" src={DEFAULT_AVATAR} />
                  : <img className={styles.avatarIcon} alt="" src={info.avatar} />
              }
            </div>

            {
              <div>
                <HabrolinkerTextField key={"avatar"} label="Ссылка на аватар"
                  placeholder="http://sm.ign.com/ign_nordic/cover/a/avatar-gen/avatar-generations_prsz.jpg"
                  onChangeValue={onAvatar} value={info.avatar == "" ? null : info.avatar} />
                <HabrolinkerTextField key={"fullname"} label="Полное имя" placeholder="Полное имя"
                  onChangeValue={onFullname} value={info.fullname} />
                <HabrolinkerEnumField key={"gender"} label="Пол" enumeration={genderEnum} value={info.gender == null ? 1 : info.gender % 2}
                  onChangeValue={onGender} />
                <HabrolinkerDateField key={"bday"} label="Дата рождения" onChangeValue={onBDay} value={info.birthday == "" ? null : info.birthday} />
                <HabrolinkerTextField key={"country"} label="Страна" placeholder="Страна" onChangeValue={onLocCountry} value={
                  info.location_country
                } />
                <HabrolinkerTextField key={"region"} label="Район" placeholder="Район" onChangeValue={onLocRegion} value={
                  info.location_region
                } />
                <HabrolinkerTextField key={"city"} label="Город" placeholder="Город" onChangeValue={onLocCity} value={
                  info.location_city
                } />
                <HabrolinkerNumberField key={"salary"} label="Доход (в долларах)"
                  onChangeValue={onSalary} value={
                    info.salary === null ? 1000 : info.salary
                  } />
                <HabrolinkerTextArrayField key={"speciality"} label="Cпециальности"
                  placeholder={["Fullstack Developer", "Game Developer"]}
                  onChangeValue={onSpeciality} value={info.specialities} />
                <HabrolinkerTextArrayField key={"skill"} label="Навыки" placeholder={["С++", "Python", "Git"]}
                  onChangeValue={onSkill} value={info.skills} />
              </div>
            }
          </div>
          <div className={styles.controllPart}>
            <div className={styles.createButton} onClick={onSaveEdit}>
              <b>Сохранить аккаунт</b>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
    ;
};

export default UserProfileEdit;
