import {useCallback, useEffect, useState} from "react";
import HabrolinkerHeader from "../components/HabrolinkerHeader";
import styles from "./SearchPage.module.css";
import HabrolinkerUserCard from "../components/HabrolinkerUserCard";
import {SendToBackend} from "../utils";
import HabrolinkerPageChooser from "../components/HabrolinkerPageChooser";
import HabrolinkerSearchFilters from "../components/HabrolinkerSearchFilters";

const SearchPage = () => {
    const [usersInfoArray, setUsersInfoArray] = useState([]);
    const [searchFilters, setSearchFilters] = useState({});
    const [editableSearchFilters, setEditableSearchFilters] = useState(
        {
            "page": 0,
            "source": 0,
            "habr_rating_low": 0,
            "habr_rating_high": 1000,
            "habr_karma_low": 0,
            "habr_karma_high": 1000,
            "age_low": 18,
            "age_high": 100,
            "location_country": "",
            "location_city": "",
            "location_region": "",
            "salary_low": 0,
            "salary_high": 1000000,
            "skills": [],
            "speciality": []
        }
    );
    const [pages, setPages] = useState({current: 0, amount: 0});

    useEffect(() => {
        setUsersInfoArray([]);
        async function fetchData() {
            let searchAnswer = await SendToBackend("POST", "/search", searchFilters);
            if (searchAnswer != null) {
                setUsersInfoArray(searchAnswer.persons_ids);
                setPages({current: searchAnswer.page, amount: searchAnswer.pages_amount});
            }
        }

        fetchData()
    }, [searchFilters]);

    const onSubmitClick = useCallback(() => {
        setSearchFilters(editableSearchFilters);
    }, [editableSearchFilters]);

    function onPage(data) {
        setSearchFilters((oldFilters) => ({...oldFilters, page: data}));
    }

    return (
        <div className={styles.searchPage}>
            <HabrolinkerHeader/>
            <div className={styles.pageContainer}>
                <div className={styles.searchContainer}>
                    <HabrolinkerSearchFilters onSubmitClick={onSubmitClick} filters={editableSearchFilters} filtersSetter={setEditableSearchFilters}/>
                    <div className={styles.foundedUsers}>
                        <b className={styles.title}>Результаты</b>
                        <HabrolinkerPageChooser current={pages.current} amount={pages.amount} onChangeValue={onPage}/>
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
                        <HabrolinkerPageChooser current={pages.current} amount={pages.amount} onChangeValue={onPage}/>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default SearchPage;
