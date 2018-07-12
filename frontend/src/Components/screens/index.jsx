import React from 'react';
import { ContentWrapper } from '../../Layout/components/Wrappers';

const Components = function Components() {
  return (
    <ContentWrapper title="Components">
      <div>
        Header Controlls
      </div>

      <div className="box box-clean">
        <div className="box-header">header</div>
        <div className="box-body">this is the Components</div>
        <div className="box-footer box-footer-clean clearfix">footer</div>
      </div>

    </ContentWrapper>
   );
};

export default Components;
