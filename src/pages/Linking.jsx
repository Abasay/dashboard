import React from 'react'
import { Link } from 'react-router-dom'
import Editor from './Editor'

const Linking = () => {
  return (
    <div>
      <h1 className='text-xl background-color: bg-white float:right'>
        {' '}
        Hi there, Trying to try the linking functionality
      </h1>
      <Link to='/Editor'>link up</Link>
    </div>
  )
}

export default Linking
