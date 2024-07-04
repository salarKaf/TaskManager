import './App.css'
import Header from './components/Header'
import TaskContainer from './components/TaskContainer'
import { GlobalContextProvider } from './context/context'
import HomePage from './components/HomePage' 

function App() {
  return (
    <GlobalContextProvider>
      <HomePage />
      {/* <Header />
      <TaskContainer /> */}
    </GlobalContextProvider>
  )
}

export default App
