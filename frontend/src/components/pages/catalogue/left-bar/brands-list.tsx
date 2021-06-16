import React, { useEffect } from 'react'
import { observer } from 'mobx-react-lite'
import { catalogueStore } from '../../../../store/catalogue-store'
import { useHistory } from 'react-router-dom'
import { Loader } from '../../../shared/loader/loader'
import { useQuery } from '../../../../hooks/useQuery'

export const BrandsList = observer(() => {

  const history = useHistory()
  const query = useQuery()

  useEffect(() => {
    catalogueStore.loadBrandList()
  }, [])

  return (
    <div className="card-body">
      {
        catalogueStore.isBrandListLoading ? <Loader/>
          :
          <ul className="list-menu">
            {
              catalogueStore.brandList.map(brand =>
                <li key={brand.id}>
                  <button
                    onClick={() => {
                      query.set('brand_id', catalogueStore.calcBrandIdString(brand.id))
                      history.push({ pathname: '/products/page/1', search: query.toString() })
                    }}
                    style={{ textDecoration: 'none', padding: '1px 12px' }}
                    className={`btn btn-link ${brand.id === catalogueStore.filters.brandId ? 'dark font-weight-bold' : ''}`}
                  >
                    {brand.title}
                  </button>
                </li>
              )
            }
          </ul>
      }
    </div>
  )
})

