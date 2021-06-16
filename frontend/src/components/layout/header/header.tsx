import React from 'react'
import { NavLink } from 'react-router-dom'
import { SearchForm } from './search-form'
import { cartStore } from '../../../store/cart-store'
import { Observer } from 'mobx-react-lite'

export const Header = () => {

  return (
    <>
      <header className="section-header">
        <section className="header-main border-bottom">
          <div className="container">
            <div className="row align-items-center">
              <div className="col-lg-2 col-4">
                <a href="http://bootstrap-ecommerce.com" className="brand-wrap">
                  <img className="logo" alt="" src="/images/logo.png"/>
                </a>
              </div>
              <div className="col-lg-6 col-sm-12">
                <SearchForm/>
              </div>
              <div className="col-lg-4 col-sm-6 col-12">
                <div className="widgets-wrap float-md-right">
                  <div className="widget-header  mr-3">
                    <NavLink to="/cart" className="icon icon-sm rounded-circle border"><i
                      className="fa fa-shopping-cart"/></NavLink>
                    <Observer>
                      {() => <span className="badge badge-pill badge-danger notify">{cartStore.productsCount}</span>}
                    </Observer>
                  </div>
                  <div className="widget-header icontext">
                    <a href="#" className="icon icon-sm rounded-circle border"><i
                      className="fa fa-user"/></a>
                    <div className="text">
                      <span className="text-muted">Welcome!</span>
                      <div>
                        <a href="#">Sign in</a> |
                        <a href="#"> Register</a>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
      </header>
    </>
  )
}



