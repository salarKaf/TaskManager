import React from 'react'
import { useGlobalContext } from '../context/context'

const SearchTask = () => {
  
  const { setQuery } = useGlobalContext();
  const handleChange = (e) => {
    setQuery(e.target.value);
  }
  
  return (
    <>
      <input type="text" name="text" id='search-box' placeholder="Search task..." onChange = {handleChange} />
    </>
  )
}

export default SearchTask