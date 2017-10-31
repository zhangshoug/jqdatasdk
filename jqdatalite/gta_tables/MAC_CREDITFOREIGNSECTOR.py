

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_CREDITFOREIGNSECTOR(Base):
    __tablename__ = "MAC_CREDITFOREIGNSECTOR"

    SGNMONTH = Column(String(14, u'utf8_bin'), primary_key=True)
    TOTALDEPOSIT = Column(Numeric(18, 4))
    HOUSEHOLDDEPOSIT = Column(Numeric(18, 4))
    HOUSEHOLDDEMANDDEPOSIT = Column(Numeric(18, 4))
    HOUSEHOLDTIMEDEPOSIT = Column(Numeric(18, 4))
    NONFINANCEDEPOSIT = Column(Numeric(18, 4))
    NONFINANCEDEMANDDEPOSIT = Column(Numeric(18, 4))
    NONFINANCETIMEDEPOSIT = Column(Numeric(18, 4))
    OTHERDEPOSIT = Column(Numeric(18, 4))
    OVERSEAFINANCE = Column(Numeric(18, 4))
    FOREIGNEXCHANGE = Column(Numeric(18, 4))
    BUSINESSSOURCE = Column(Numeric(18, 4))
    OVERSEABUSINESSSOURCE = Column(Numeric(18, 4))
    OTHERITEM = Column(Numeric(18, 4))
    TOTALFUNDSOURCE = Column(Numeric(18, 4))
    TOTALLOAN = Column(Numeric(18, 4))
    DOMESTICLOAN = Column(Numeric(18, 4))
    HOUSEHOLDLOAN = Column(Numeric(18, 4))
    CONSUMPTIONLOAN = Column(Numeric(18, 4))
    SHORTTERMCONSUMPTIONLOAN = Column(Numeric(18, 4))
    LONGTERMCONSUMPTIONLOAN = Column(Numeric(18, 4))
    OTHERSECTORLOAN = Column(Numeric(18, 4))
    LOANBILLFINANCE = Column(Numeric(18, 4))
    SHORTTERMLOAN = Column(Numeric(18, 4))
    BILLFINANCE = Column(Numeric(18, 4))
    MEDIUMLONGTERMLOAN = Column(Numeric(18, 4))
    OTHERLOAN = Column(Numeric(18, 4))
    OVERSEALOAN = Column(Numeric(18, 4))
    PORTFOLIOINVEST = Column(Numeric(18, 4))
    SECURITY = Column(Numeric(18, 4))
    OTHERSHARE = Column(Numeric(18, 4))
    BUSINESSUSE = Column(Numeric(18, 4))
    OVERSEABUSINESSUSE = Column(Numeric(18, 4))
    TOTALFUNDUSE = Column(Numeric(18, 4))
    DOMESTICDEPOSIT = Column(Numeric(18, 4))
    GOVERNMENTDEPOSIT = Column(Numeric(18, 4))
    FISCALDEPOSIT = Column(Numeric(18, 4))
    ORGANIZEDEPOSIT = Column(Numeric(18, 4))
    NONDEPOSITFINANCEDEPOSIT = Column(Numeric(18, 4))
    OVERSEADEPOSIT = Column(Numeric(18, 4))
    FINANCEBONDS = Column(Numeric(18, 4))
    REPO = Column(Numeric(18, 4))
    BORROWINGNONBANKFINANCE = Column(Numeric(18, 4))
    HOUSEHOLDSHORTTERMLOAN = Column(Numeric(18, 4))
    SHORTTERMOPERATLOAN = Column(Numeric(18, 4))
    HOUSEHOLDMIDLONGTERMLOAN = Column(Numeric(18, 4))
    HOUSEHOLDMIDLONGOPERATLOAN = Column(Numeric(18, 4))
    FINANCELEASE = Column(Numeric(18, 4))
    ADVANCE = Column(Numeric(18, 4))
    NONDEPOSITFINANCELOAN = Column(Numeric(18, 4))
    REVERSEREPO = Column(Numeric(18, 4))
    DUENONBANKFINANCEDEPOSIT = Column(Numeric(18, 4))