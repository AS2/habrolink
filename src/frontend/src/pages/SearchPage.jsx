import { useCallback, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Header from "../components/Header";
import FiltersBlock from "../components/FiltersBlock";
import User1 from "../components/User1";
import styles from "./SearchPage.module.css";

const SearchPage = () => {
  const navigate = useNavigate();
  const array = [];
  const [usersInfoArray, setUsersInfoArray] = useState([]);

  const onTextClick = useCallback(() => {
    navigate("/");
  }, [navigate]);

  const onInterfaceEssentialBookmarkIconClick = useCallback(() => {
    navigate("/saved-users");
  }, [navigate]);

  const onInterfaceEssentialChat1IconClick = useCallback(() => {
    navigate("/chats-page");
  }, [navigate]);

  const onInterfaceEssentialMagnifierClick = useCallback(() => {
    navigate("/search-page");
  }, [navigate]);

  const onLilProfileClick = useCallback(() => {
    navigate("/user-profile");
  }, [navigate]);

  const onSendMessageContainerClick = useCallback(() => {
    // Please sync "Message page" to the project
    console.log("submited something");
  }, []);

  const onInfoContainerClick = useCallback(() => {
    // Please sync "Other user1 info" to the project
  }, []);

  const onSendMessageContainer2Click = useCallback(() => {
    // Please sync "Recived message page" to the project
  }, []);

  const onInfoContainer2Click = useCallback(() => {
    // Please sync "Other user2 info" to the project
  }, []);

  const onSendMessageContainer3Click = useCallback(() => {
    // Please sync "Recived message page" to the project
  }, []);

  const onInfoContainer3Click = useCallback(() => {
    // Please sync "Other user3 info" to the project
  }, []);


  const onSubmitClick = useCallback(() => {
    console.log(usersInfoArray, usersInfoArray.length);

    setUsersInfoArray(usersInfoArray.concat([{
      "intersect": "/intersect.svg",
      "prop": "Артур Шелби",
      "nickname": "@big_bro",
      "karma": "Карма: 140",
      "rating": "Рейтинг: 4.9",
      "softKittyLovermailcom": "soft_kitty_lover@mail.com",
      "interfaceEssentialBookmar": "/interface-essentialbookmark1.svg"
    }]))
    usersInfoArray.push({
      "intersect": "/intersect.svg",
      "prop": "Артур Шелби",
      "nickname": "@big_bro",
      "karma": "Карма: 140",
      "rating": "Рейтинг: 4.9",
      "softKittyLovermailcom": "soft_kitty_lover@mail.com",
      "interfaceEssentialBookmar": "/interface-essentialbookmark1.svg"
    })
  }, []);

  return (
    <div className={styles.searchPage}>
      <Header
        onTextClick={onTextClick}
        onInterfaceEssentialBookmarkIconClick={
          onInterfaceEssentialBookmarkIconClick
        }
        onInterfaceEssentialChat1IconClick={onInterfaceEssentialChat1IconClick}
        onInterfaceEssentialMagnifierClick={onInterfaceEssentialMagnifierClick}
        onLilProfileClick={onLilProfileClick}
      />
      <div className={styles.pageContainer}>
        <b className={styles.title}>Поиск</b>
        <div className={styles.searchContainer}>
          <FiltersBlock
            onSubmitClick={onSubmitClick}
          />

          <div className={styles.foundedUsers}>
            <b className={styles.title}>Результаты</b>
            <div id="searchingResult">
              <User1
                intersect="/intersect.svg"
                prop="Артур Шелби"
                nickname="@big_bro"
                karma="Карма: 140"
                rating="Рейтинг: 4.9"
                softKittyLovermailcom="soft_kitty_lover@mail.com"
                interfaceEssentialBookmar="/interface-essentialbookmark1.svg"
                showDot1
                showKarma
                showDot2
                showRating
                onSendMessageContainerClick={onSendMessageContainerClick}
                onInfoContainerClick={onInfoContainerClick}
              />
              {usersInfoArray.map((info, index) => (
                <User1
                  intersect={info["intersect"]}
                  prop={info["prop"]}
                  nickname={info["nickname"]}
                  karma={info["karma"]}
                  rating={info["rating"]}
                  softKittyLovermailcom={info["softKittyLovermailcom"]}
                  interfaceEssentialBookmar={info["interfaceEssentialBookmar"]}
                  showDot1
                  showKarma
                  showDot2
                  showRating
                  onSendMessageContainerClick={onSendMessageContainerClick}
                  onInfoContainerClick={onInfoContainerClick}
                />
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SearchPage;
