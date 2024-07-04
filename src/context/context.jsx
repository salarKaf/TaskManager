import { createContext, useContext, useReducer, useState } from "react";
import { tasksReducer } from "./reducers";

const GlobalContext = createContext();
export const GlobalContextProvider = ({children}) => {
  const [tasksState, tasksDispatch] = useReducer(tasksReducer, {
    tasks: []
  })
  
  const [query, setQuery] = useState("");   // We could have used useReducer here as well but this case is simple and we don't have much complex logic here.
  return <GlobalContext.Provider value={{tasksState, tasksDispatch, query, setQuery}}>{children}</GlobalContext.Provider>
}

export const useGlobalContext = () => {
  return useContext(GlobalContext);
}