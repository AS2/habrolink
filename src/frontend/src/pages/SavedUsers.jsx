import {useCallback, useEffect, useState} from "react";
import HabrolinkerHeader from "../components/HabrolinkerHeader";
import styles from "./SavedUsers.module.css";
import HabrolinkerUserCard from "../components/HabrolinkerUserCard";
import {SendToBackend, SendToBackendAuthorized} from "../utils";

const SavedUsers = () => {
  const [usersInfoArray, setUsersInfoArray] = useState([]);

  useEffect(() => {
    setUsersInfoArray([]);
    async function fetchData() {
      let searchAnswer = await SendToBackendAuthorized("POST", "/mark/list", {});
      if (searchAnswer != null) {
        setUsersInfoArray(searchAnswer.persons_ids);
      }
    }

    fetchData()
  }, []);

  return (
    <div className={styles.savedUsers}>
      <HabrolinkerHeader/>
      <div className={styles.pageContainer}>
        <b className={styles.title}>Сохраненные пользователи</b>
        <div className={styles.searchContainer}>
          <div className={styles.foundedUsers}>
          {usersInfoArray.length > 0
              ? <div className={styles.searchResult}>
                {usersInfoArray.map((personId, index) => (
                    <HabrolinkerUserCard
                        key={personId}
                        personId={personId}
                    />
                ))}
              </div>
              : <b className={styles.title}> Пусто &#128577; </b>
          }
          </div>
        </div>
      </div>
    </div>
  );
};

export default SavedUsers;
